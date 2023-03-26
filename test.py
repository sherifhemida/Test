#list subfolder names in the current directory
import os
for name in os.listdir('.'):
    if os.path.isdir(name):
        print(name)

#print date time
import datetime
print (datetime.datetime.now())