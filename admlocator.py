#!/usr/bin/env python2

import sys
import os
import httplib
import socket

#General Stuffs start
def banner():
        print '''
                                                                                        
       .oo      8          o       o                            o        
      .P 8      8                  8                            8         
     .P  8 .oPYo8 ooYoYo. o8 odYo. 8     .oPYo. .oPYo. .oPYo.  o8P .oPYo. oPYo
    oPooo8 8    8 8' 8  8  8 8' `8 8     8    8 8    ' .oooo8   8  8    8 8  `
   .P    8 8    8 8  8  8  8 8   8 8     8    8 8    . 8    8   8  8    8 8   
  .P     8 `YooP' 8  8  8  8 8   8 8oooo `YooP' `YooP' `YooP8   8  `YooP' 8   
  ..:::::..:.....:..:..:..:....::........:.....::.....::.....:::..::.....:..::
  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                        ver.2.1 (-) Mr.Geek (-) 4Sectors
                            Recoded by thixpin
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
                cmd = 'cls && color 0A'
        os.system(cmd)

def MSG(msg):
        if msg == 'adminrun':
                print('[*] Starting Admin Locator ...')
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
        adminwl = 'all.txt'
        adminwl1 = 'php.txt'
        adminwl2 = 'asp.txt'
        adminwl3 = 'cfm.txt'
        adminwl4 = 'js.txt'
        adminwl5 = 'cgi.txt'
        adminwl6 = 'brf.txt'

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
                                print ("\t [#] Checking " + self.url + self.path )
                                conn = httplib.HTTPConnection(self.url) 
                                conn.request("GET",self.path)
                                resp = conn.getresponse()
                                if resp.status == 200:
                                        MSG('found')
                                        print '[-]> %s%s'%(self.url,self.path)
                                        raw_input("Press enter to continue scanning.\n")
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
                                   print '[~] Exiting ... \n'
                                   self.printf()
                                   sys.exit(0)
                                   
                except Exception,e:
                                print('[*] General Error occurs ...')
                                print('[-] Terminating ...')
                                sys.exit(0)
        
        def run(self):
                MSG('adminrun')

        def printf(self):
                clear()
                banner()
                print '\n \n \t Scan Conpleted for Target: ' + self.url + ' \n '
                print '\t [*] Total Found Admin page or pages (-)> %s'%(self.count)
                print self.foundpaths
                print '\n \n'
                                
#Classes end
#Functions start
def main():
        try:
                site = raw_input("Web Site for Scan?: ")
                site = site.replace("http://","")
                print ("\tChecking website " + site + "...")
                conn = httplib.HTTPConnection(site)
                conn.connect()
                print "\t[$] Yes... Server is Online."
        except (httplib.HTTPResponse, socket.error) as Exit:
                raw_input("\t [!] Oops Error occured, Server offline or invalid URL")
                exit()
        print "Enter site source code:"
        print "1 PHP"
        print "2 ASP"
        print "3 CFM"
        print "4 JS"
        print "5 CGI"
        print "6 BRF"
        print "7 All"
        print "\nPress 1 and 'Enter key' for Select PHP\n"
        ec=input("> ")
        AdminLocator(site,ec)
        
def AdminLocator(domain,ec):
        '''Admin Finder function'''
        url = domain
        code = ec
        if code==1:
                b = Bruter(url,wordlist.adminwl1)
        if code==2:
                b = Bruter(url,wordlist.adminwl2)
        if code==3:
                b = Bruter(url,wordlist.adminwl3)
        if code==4:
                b = Bruter(url,wordlist.adminwl4)
        if code==5:
                b = Bruter(url,wordlist.adminwl5)
        if code==6:
                b = Bruter(url,wordlist.adminwl6)
        if code==7:
                b = Bruter(url,wordlist.adminwl)
        b.run()
        b.brute()
        b.printf()
        pass

#Functions end


if __name__ == "__main__":
        clear()
        banner()
        main()
