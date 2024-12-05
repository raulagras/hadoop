#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    try:
        data = line.strip().split("\t")
        if len(data) == 6:
            _, _, store, _, cost, _ = data
            print(store + "\t" + cost)
        else:
            continue
    except Exception:
        continue
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        data = line.strip().split("\t")
        if len(data) == 6:
            _, _, store, _, cost, _ = data
            print(store + "\t" + cost)
        else:
            # Ignoramos líneas con formato incorrecto
            continue
    except Exception:
        # Si ocurre algún error al procesar una línea, se ignora
        continue
