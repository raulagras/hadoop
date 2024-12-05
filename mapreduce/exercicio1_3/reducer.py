#!/usr/bin/env python

import sys

max_sale = 0
old_payment_type = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    this_payment_type, this_cost = data

    if old_payment_type and old_payment_type != this_payment_type:
        print(old_payment_type + "\t" + str(max_sale))
        old_payment_type = this_payment_type
        max_sale = 0

    old_payment_type = this_payment_type
    max_sale = max(max_sale, float(this_cost))

if old_payment_type is not None:
    print(old_payment_type + "\t" + str(max_sale))
