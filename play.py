import subprocess
import sys, glob
player = None
locked = True
while True:
    print "player ready:",
    code = raw_input()
    for filename in glob.glob("*"):
        parts = filename.split("-")
        if code != parts[0]:
            continue
        if player:
           player.terminate()
           player = None
        if len(parts) == 1:
            continue
        if parts[1] == "key":
            locked = not locked 
            if locked:
                print "now locked" 
            else:
                print "now unlocked" 
        elif parts[1] == "stop":
            continue
        elif locked:
            print "locked!"	
        else:
            print "playing ", filename
            player = subprocess.Popen(["play","-q", filename], stdin=subprocess.PIPE, stdout=sys.stdout,stderr=sys.stdout,bufsize=1)
