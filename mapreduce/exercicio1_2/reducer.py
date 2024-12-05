#!/usr/bin/env python

import sys

sales_total = 0
old_category = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    this_category, this_cost = data

    if old_category and old_category != this_category:
        print(old_category + "\t" + str(sales_total))
        old_category = this_category
        sales_total = 0

    old_category = this_category
    sales_total += float(this_cost)

if old_category is not None:
    print(old_category + "\t" + str(sales_total))
