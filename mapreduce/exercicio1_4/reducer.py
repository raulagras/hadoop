#!/usr/bin/env python

import sys

max_sale = 0

for line in sys.stdin:
    try:
        _, this_cost = line.strip().split("\t")
        max_sale = max(max_sale, float(this_cost))
    except Exception:
        continue

print("Max Sale\t" + str(max_sale))
