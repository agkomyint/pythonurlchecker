import subprocess
import os

#make a url text file here and add here:3
with open("urls.txt","r") as file:
    x=" ".join([content.strip() for content in file])
    y=x.split()
    print(y)

#for windows user you should change ping to ping.exe incase if its not work.in subprocess.Popen inside.
with open(os.devnull, "wb") as limbo:
        for host in y:
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", host],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (host, " is not available")
                else:
                        print (host, "is working")
