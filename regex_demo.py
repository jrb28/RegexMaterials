# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:23:20 2023

@author: jrbrad
"""

import re

with open('regex_video_text.txt', 'r') as f:
    string = f.read()

regex_pattern = '(\(|1-|[ ]*)(\d{3})(\) |\.|-)(\d{3})(-|\.)(\d{4})'
#regex_pattern = '\d*\.\d+|\d+\.?'
#regex_pattern = '(R|r)eg(E|e)x'
results = re.findall(regex_pattern, string)
results = [''.join(r) for r in results]
print(results)