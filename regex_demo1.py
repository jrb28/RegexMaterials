# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:23:20 2023

@author: jrbrad
"""

import re

with open('regex_video_text.txt', 'r') as f:
    string = f.read()

regex_pattern = '[Rr]eg[Ee]x'
results = re.findall(regex_pattern, string)

print(results)