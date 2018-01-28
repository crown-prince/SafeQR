# -*- coding: utf-8 -*-
import hashlib
import sys 

def main():
    filename = "test.jpg"
    m = hashlib.md5()
    with open(filename, 'rb') as fp: 
        while True:
            blk = fp.read(4096) # 4KB per block
            if not blk: break
            m.update(blk) #m.hexdigest(), filename
    #比对白名单
    flag = 0
    WhiteMd5 = list() 
    for line in open("Md5.db"):
        WhiteMd5.append(line.strip())
        #print line
    for test in WhiteMd5:
        if test == m.hexdigest():
            print "%s must be a Safe URl" % (filename)
            flag = 1
    if flag == 0:
        print "Score - 10"
if __name__ == '__main__':
    main()
