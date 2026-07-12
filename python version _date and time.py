 import sys
 print("python version")
 print(sys.version)

import datetime
now=datetime.datetime.now() #class inside module
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S")) #string format time(strftime)
