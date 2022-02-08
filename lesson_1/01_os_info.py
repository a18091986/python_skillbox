#Нужно собрать информацию об операционной системам и версии Python

#TODO запустить этот скрипт и закоммитить результат его работы (файл os_info.txt)

import platform
import sys

info = f'OS info is \n{platform.uname()}\n' \
       f'Python version is {sys.version}, {platform.architecture()}'
print(info)

with open('os_info.txt', 'w') as f:
    f.write(info)

