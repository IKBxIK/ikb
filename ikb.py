import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import ikb
if bit == '32bit':
    os.system('clear')
     print('32 bit will be updated Soon')
