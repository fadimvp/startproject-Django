import webbrowser
import os
import time


t= 3
c=0
while c < t :
    c = c + 1

    if c ==1 :
        print "open befor 30 Minute"
        time.sleep(60*30)

        webbrowser.open("https://www.youtube.com/watch?v=RMK5xovn0u8")
