# -*- coding: utf-8 -*-
import zbar
from PIL import Image

score = 100

scanner = zbar.ImageScanner()
scanner.parse_config('enable')
img = Image.open('./test2.jpg').convert('L')
w , h = img.size
raw = img.tostring()
zimg = zbar.Image(w, h, 'Y800', raw)

scanner.scan(zimg)

for s in zimg:
    print "The %s is: %s" %(s.type, s.data)
    
#提取域名
domain = ""
flag = 0
begin = 0
end = 0
j = 0
for i in s.data:
    if flag == 0 and i == '/':
        begin = j + 2
        flag = 1
    elif flag == 1 and i == '/':
        flag = 2
    elif flag == 2 and i == '/':
        end = j - 1
        break
    j = j + 1
#print begin
#print end
domain = s.data[begin:end + 1]
print "The Domain is: %s" %(domain)
        
#比对白名单
flag = 0
WhiteUrl = list()
for line in open("WhiteList.config"):
    WhiteUrl.append(line.strip())
    #print line
for test in WhiteUrl:
    if test == domain:
        print "%s must be a Safe URl" % (test)
        flag = 1
if flag == 0:
    print "Score - 10"
