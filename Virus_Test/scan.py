# encoding: UTF-8
#

import httplib, mimetypes
import urllib
import urllib2
import os
import sys
import optparse
import hashlib
import socket
import time
import uuid

# The apikey.
API_KEY = "3a0e11e2d24e4d79a7e4bf39084067b1e6200d7aff9b43ce9077bffe86d64f69"

FILE_SIZE_LIMIT = 100 * 1024 * 1024   # 100MB

class postfile:
    @staticmethod
    def post_multipart(host, selector, fields, files):
        content_type, body = postfile.encode_multipart_formdata(fields, files)
        if selector.lower().startswith("https://"):
            h = httplib.HTTPS(host)
        else:
            h = httplib.HTTP(host)
        h.putrequest('POST', selector)
        h.putheader('content-type', content_type)
        h.putheader('content-length', str(len(body)))
        h.endheaders()
        h.send(body)
        errcode, errmsg, headers = h.getreply()

        try:
            ret = h.file.read()
        except Exception, e:
            print "Error - post_multipart"
            return False

        return ret

    @staticmethod
    def encode_multipart_formdata(fields, files):
        BOUNDARY = '----------' + str(uuid.uuid1()).replace('-', '')
        CRLF = '\r\n'
        L = []
        for (key, value) in fields:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"' % key)
            L.append('')
            L.append(value)
        for (key, filename, value) in files:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
            L.append('Content-Type: %s' % postfile.get_content_type(filename))
            L.append('')
            L.append(value)
        L.append('--' + BOUNDARY + '--')
        L.append('')
        body = CRLF.join((bytes(i) for i in L))
        content_type = 'multipart/form-data; boundary=%s' % BOUNDARY

        return content_type, body

    @staticmethod
    def get_content_type(filename):
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

class ThreatBook(object):

    def __init__(self, api_key):

        super(ThreatBook, self).__init__()

        self.api_key = api_key

    def __repr__(self):
        return "<ThreatBook proxy>"

    def get(self, filename, content):
        print "Getting the report ..., return the result after 3 seconds.\r\n"
        time.sleep(3)

        sha256 = hashlib.sha256(content).hexdigest()

        url = "https://x.ThreatBook.cn/api/v1/file/report"
        
        parameters = {"resource": sha256,
                       "apikey": self.api_key,
                       "dev_id": "test_device",
                       "path": filename}
        data = urllib.urlencode(parameters)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        ret_json = response.read()

        print "Report(in JSON):\r\n"

        print ret_json
        return 1;

    def scan(self, filename, content):
        print "File uploading ...\r\n"

        # scan the file
        host = "x.threatbook.cn"
        selector = "https://x.threatbook.cn/api/v1/file/scan"
        #host = "localhost:9000"
        #selector = "http://localhost:9000/api/v1/file/scan"
        fields = [("apikey", self.api_key),("dev_id","test_device")]
        files = [("file", filename, content)]
        ret_json = postfile.post_multipart(host, selector, fields, files)

        if False == ret_json:
            print "Upload failed!"
            return False
        else:
            print "Upload succeed, the response (in JSON):\r\n"
            print ret_json
            return True

def main():
    parser = optparse.OptionParser(usage = """
    %prog <file_path>
Samples:
    %prog c:\\virus\\test.exe
    """)

    (options, arguments) = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_usage()
        return -1

    filepath = arguments.pop(0)
    if not os.path.exists(filepath):
        print "Error: file not found."
        return -1

    filesize = os.path.getsize(filepath)
    if filesize == 0:
        print "Error: file size is 0."
        return -1;
    if filesize > FILE_SIZE_LIMIT:
        print "Error: file size beyond the limitation: 50MB."
        return -1;

    content = open(filepath, "rb").read()
    filename = os.path.basename(filepath)

    timeout = 300
    socket.setdefaulttimeout(timeout)

    v = ThreatBook(API_KEY)
    v.scan(filepath, content)
    print
    v.get(filename, content)


if __name__ == "__main__":
    main()