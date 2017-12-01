#!/usr/bin/env python3

import nbp
import json

print('\n--- get_tables ---\n')

text = nbp.get_tables()
if text:
    data = json.loads(text)
    nbp.display_table(data)

print('\n--- get_tables / today ---\n')

text = nbp.get_tables(today=True)
if text:
    data = json.loads(text)
    nbp.display_table(data)

print('\n--- get_tables / date=2017-04-06 ---\n')

text = nbp.get_tables(date='2017-04-06')
if text:
    data = json.loads(text)
    nbp.display_table(data)

print('\n--- get_tables / table=C ---\n')

text = nbp.get_tables(table='C', date='2017-04-06')
if text:
    data = json.loads(text)
    nbp.display_table(data)

print('\n--- get_rates / table=C ---\n')

text = nbp.get_rates(table='C', date='2017-04-06')#, show_url=True)
if text:
    data = json.loads(text)
    nbp.display_rates(data)

print('\n--- get_tables / invalid date ---\n')

nbp.DEBUG = True # display error message 

text = nbp.get_tables(table='C', date='2017-12-31')
if text:
    data = json.loads(text)
    nbp.display_tables(data)

# for date '2017-12-31'
# DEBUG: request error: HTTP Error 400: B³êdny zakres dat / Invalid date range
#
# for date '2017-12-32'
# DEBUG: request error: HTTP Error 404: Not Found

help(nbp)
