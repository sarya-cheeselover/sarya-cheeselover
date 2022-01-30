#!/usr/bin/env python3

import os
from datetime import datetime


entries = os.listdir()
now = datetime.now()
print (now.strftime("%H:%M:%S"))


with open ("PATH TO FILE TO ADD THE TIMESTAMP","a") as file:
    file.write("Time now is: "+ now.strftime("%H:%M:%S")+"\n")

file.close()
