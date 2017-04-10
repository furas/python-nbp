#!/usr/bin/env python3

import nbp
import json

text = nbp.get_tables()
if text:
    data = json.loads(text)
    for table in data:
        nbp.display_table(table)

text = nbp.get_tables(today=True)
if text:
    data = json.loads(text)
    for table in data:
        nbp.display_table(table)

text = nbp.get_tables(date='2017-04-06')
if text:
    data = json.loads(text)
    for table in data:
        nbp.display_table(table)

text = nbp.get_tables(table='C', date='2017-04-06')
if text:
    data = json.loads(text)
    for table in data:
        nbp.display_table_c(table)

text = nbp.get_rates(table='C', date='2017-04-06')#, show_url=True)
if text:
    data = json.loads(text)
    nbp.display_rates_c(data)
