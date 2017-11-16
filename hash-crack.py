print '''
######################################################################################################
# ________  ________  __    __  _______    ______         ________  ________   ______   __       __  #     
#|        \|        \|  \  |  \|       \  /      \       |        \|        \ /      \ |  \     /  \ #     
# \$$$$$$$$| $$$$$$$$| $$\ | $$| $$$$$$$\|  $$$$$$\       \$$$$$$$$| $$$$$$$$|  $$$$$$\| $$\   /  $$ #     
#   | $$   | $$__    | $$$\| $$| $$  | $$| $$___\$$         | $$   | $$__    | $$__| $$| $$$\ /  $$$ #     
#   | $$   | $$  \   | $$$$\ $$| $$  | $$ \$$    \          | $$   | $$  \   | $$    $$| $$$$\  $$$$ #     
#   | $$   | $$$$$   | $$\$$ $$| $$  | $$ _\$$$$$$\         | $$   | $$$$$   | $$$$$$$$| $$\$$ $$ $$ #     
#   | $$   | $$_____ | $$ \$$$$| $$__/ $$|  \__| $$         | $$   | $$_____ | $$  | $$| $$ \$$$| $$ #     
#   | $$   | $$     \| $$  \$$$| $$    $$ \$$    $$         | $$   | $$     \| $$  | $$| $$  \$ | $$ #     
#    \$$    \$$$$$$$$ \$$   \$$ \$$$$$$$   \$$$$$$           \$$    \$$$$$$$$ \$$   \$$ \$$      \$$ #     
#                                                                                                    #     
#                  Coded by : Ismael Al-safadi           * hash cracker *                            #
######################################################################################################
                                                                                                         


'''

import getopt
import hashlib
import sys
import os
import time

def sound():
    try:
        import winsound
        winsound.Beep(1000,1000)
        
    except:
        pass

def info():

  print "Information"
  print "[*] Options:"
  print "[*](-h) Hash"
  print "[*](-t) Type"
  print "[*](-w) Wordlist"
  print "[*] Examples:"
  print "[>] python hash-crack.py -h <hash> -t md5 -w passwordlist.txt"
  print "[>] python hash-crack.py -h ed2b1f468c5f915f3f1cf75d7068baae -t md5 -w passwordlist.txt"
  print "[*] Supported Hashes:"
  print "[>] md5, sha1, sha224, sha256, sha384, sha512"
  print "[*] ^__^ "
  print "[*] Coded By : Ismael Al-safadi"
  

class hashCracking:
  
  def hashCrackWordlist(self, userHash, hashType, wordlist):
    start = time.time()
    self.lineCount = 0
    if (hashType == "md5"):
       h = hashlib.md5
    elif (hashType == "sha1"):
       h = hashlib.sha1
    elif (hashType == "sha224"):
       h = hashlib.sha224
    elif (hashType == "sha256"):
       h = hashlib.sha256
    elif (hashType == "sha384"):
       h = hashlib.sha384
    elif (hashType == "sha512"):
       h = hashlib.sha512
    else:
       print "[-]Ops %s  is ont supported hash type ." % hashType
       exit()
    with open(wordlist, "rU") as infile:
      for line in infile:
        line = line.strip()
        lineHash = h(line).hexdigest()
        if (lineHash == userHash.lower()):
            end = time.time()
            print "\n[+]Hash is: %s" % line
            print "[*]Words tried: %s" % self.lineCount
            print "[*]Time: %s seconds" % round((end-start), 2)
            sound()
            exit()
        else:
            self.lineCount = self.lineCount + 1
    end = time.time()
    print "\n[-]Cracking Failed"
    print "[*]Reached end of wordlist"
    print "[*]Words tried: %s" % self.lineCount
    print "[*]Time: %s seconds" % round((end-start), 2)
    exit()

def main(argv):
  hashType = userHash = wordlist  = numbersBruteforce = None
  
  try:
      opts, args = getopt.getopt(argv,"ih:t:w:nv",["ifile=","ofile="])
  except getopt.GetoptError:
      print '[*]python hash-crack.py -t <type> -h <hash> -w <wordlist>'
      print '[*]Type python hash-crack.py -i for information'
      sys.exit(1)
  for opt, arg in opts:
      if opt == '-i':
          info()
          sys.exit()
      elif opt in ("-t", "--type"):
          hashType = arg
      elif opt in ("-h", "--hash"):
          userHash = arg
      elif opt in ("-w", "--wordlist"):
          wordlist = arg
      
  if not (hashType and userHash):
      info()
      sys.exit()
  print "[*]Hash: %s" % userHash
  print "[*]Hash type: %s" % hashType
  print "[*]Wordlist: %s" % wordlist
  print "[+]Cracking..."
  

  try:
      h = hashCracking()
      h.hashCrackWordlist(userHash, hashType, wordlist)

  except IndexError:
        print "\n[-]Hash not cracked:"
        print "[*]Reached end of wordlist"
        print "[*]Try another wordlist"
        print "[*]Words tried: %s" % h.lineCount
        
  except KeyboardInterrupt:
        print "\n[Exiting...]"
        print "Words tried: %s" % h.lineCount
        
  except IOError:
        print "\n[-]Couldn't find wordlist"
        print "[*]Is this right?"
        print "[>]%s" % wordlist
        
if __name__ == "__main__":
    main(sys.argv[1:])
