#!/usr/bin/env python

import sys

total_sales = 0

for line in sys.stdin:
    try:
        _, this_cost = line.strip().split("\t")
        total_sales += float(this_cost)
    except Exception:
        continue

print("Total Sales\t" + str(total_sales))
