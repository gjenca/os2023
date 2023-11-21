#!/usr/bin/env python3

import sys

count=0
for line in sys.stdin:

    if "bum" in line:
        count=count+1

print(count,'lines with bums')


