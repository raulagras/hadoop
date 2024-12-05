#!/usr/bin/env python

import sys

for line in sys.stdin:
    try:
        data = line.strip().split("\t")
        if len(data) == 6:
            _, _, _, _, cost, payment = data
            print(payment + "\t" + cost)
    except Exception:
        continue
