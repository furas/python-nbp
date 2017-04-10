#!/usr/bin/env python3

import nbp

text = nbp.get_table()
nbp.display_table(text)

text = nbp.get_table(today=True)
nbp.display_table(text)

text = nbp.get_table(date='2017-04-06')
nbp.display_table(text)
