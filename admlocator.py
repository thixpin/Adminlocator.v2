#!/usr/bin/env python2

import sys
import os
import httplib

#General Stuffs start
def banner():
        print '''
                                                                                         
                .oo      8          o       o                            o               
               .P 8      8                  8                            8               
              .P  8 .oPYo8 ooYoYo. o8 odYo. 8     .oPYo. .oPYo. .oPYo.  o8P .oPYo. oPYo. 
             oPooo8 8    8 8' 8  8  8 8' `8 8     8    8 8    ' .oooo8   8  8    8 8  `' 
            .P    8 8    8 8  8  8  8 8   8 8     8    8 8    . 8    8   8  8    8 8     
           .P     8 `YooP' 8  8  8  8 8   8 8oooo `YooP' `YooP' `YooP8   8  `YooP' 8     
           ..:::::..:.....:..:..:..:....::........:.....::.....::.....:::..::.....:..::::
           ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
           ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                   ver.2 (-) Mr.Geek (-) 4Sectors
        '''
def usage():
        print '''
                :: Usage ::
                $ ./adminlocator.py -u <url>
                <url> format ==> http://www.google.com  ,etc.
        '''

def clear():
        if os.name == 'posix':
                cmd = 'clear'
        else:
                cmd = 'cls'
        os.system(cmd)

def MSG(msg):
        if msg == 'adminrun':
                print('[*] Starting Admin Locator ...')
                print('[-] Brute forcing admin paths (-)> %s'%(sys.argv[2]))
        elif msg == 'found':
                print('[!] Found Admin page @> ')
        elif msg == 'redirect':
                print('[!] Redirecting path ... ')
        elif msg == 'forbidden':
                print('[!] Forbidden path ... ')
        else:
                return none

#General Stuffs end
#Classes start
class wordlist:
        adminwl = 'admins.txt'

class Bruter(object):
        def __init__(self,url,wordlist):
                if '://' in url:
                        self.url = url.replace("http://","")
                else :  self.url = url
                self.wordlist = wordlist
                self.filecontent = self.readwl()
                self.count = 0
                self.foundpaths = []
                
        def readwl(self):
                try:
                    lines = [line.strip() for line in open(self.wordlist)]
                    return lines
                except IOError:
                    print 'couldn\'t open file...'
                    sys.exit(0)
        
        def brute(self):
                try:
                        for path in self.filecontent:
                           try:
                                self.path = "/"+path
                                conn = httplib.HTTPConnection(self.url)
                                conn.request("GET",self.path)
                                resp = conn.getresponse()
                                if resp.status == 200:
                                        MSG('found')
                                        print '[-]> %s%s'%(self.url,self.path)
                                        self.count += 1
                                        self.foundpaths.append('%s%s'%(self.url,self.path))
                                elif resp.status == 302:
                                        MSG('redirect')
                                        print '[-]> %s%s'%(self.url,self.path)
                                elif resp.status == 403:
                                        MSG('forbidden')
                                else:
                                        pass
                           except KeyboardInterrupt:
                                   print '[~] KeyboardInterrupt'
                                   print '[~] Exiting ...'
                                   self.printf()
                                   sys.exit(0)
                                   
                except Exception,e:
                                print('[*] General Error occurs ...')
                                print('[-] Terminating ...')
                                sys.exit(0)
                
        def run(self):
                MSG('adminrun')

        def printf(self):
                print '=========================================='
                print '[*] Total Found Admin page or pages (-)> %s'%(self.count)
                print self.foundpaths                
                                
#Classes end
#Functions start        
def AdminLocator(domain):
        '''Admin Finder function'''
        url = domain
        b = Bruter(url,wordlist.adminwl)
        b.run()
        b.brute()
        b.printf()
        pass

#Functions end

def main():
        '''Main function'''
        if len(sys.argv) == 3 and sys.argv[1] == '-u' and sys.argv[2].startswith('http://'):
                AdminLocator(sys.argv[2])

        else:
                usage()

#Py_ver = sys.version.split()[0]#testing...

if __name__ == "__main__":
        clear()
        banner()
        main()
