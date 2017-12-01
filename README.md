
Exchange rates from NBP (Narodowy Bank Polski - Polish National Bank)

API: http://api.nbp.pl/ (PL), http://api.nbp.pl/en.html (EN)

**Examples in CLI**

```bash
$ nbp.py -h
$ python3 -m nbp -h

usage: nbp.py [-h] [-t TABLE] [-c CODE] [-d DATE] [-l NUMBER] [--today]
              [--from FROM_DATE] [--to TO_DATE] [--json] [--xml] [--url]
              [--debug]


Get data from NBP
 
optional arguments:
  -h, --help        show this help message and exit
  -t TABLE          table name: A, B or C (default: A)
  -c CODE           code of currency
  -d DATE           table for date DATE
  -l NUMBER         last NUMBER tables
  --today           table for exactly today
  --from FROM_DATE  tables from FROM_DATE to TO_DATE
  --to TO_DATE      tables from FROM_DATE to TO_DATE
  --json            return json
  --xml             return xml
  --url             show url
  --debug           show arguments
 
Date format: YYYY-MM-DD
 
Some arguments may return no data

$ nbp.py -t C -c usd -l 5 --xml --url

$ python3 -m nbp -t C -c usd -l 5 --xml --url
```

**Examples in code**

```python
import nbp

text = nbp.get_rates(table='C', code='usd', last=5, format='xml', show_url=True)
print(text)

text = nbp.get_tables(table='A', code='usd', last=5)
if text:
  data = json.loads(text)
  print(data[0])
```

---

When function can't get data then it returns `None` instead of raising exception. 
You have to check `None` before you 

You can set `npb.DEBUG = True` to see error message raised by request.

Example with invalid date `2017-12-32`

```python
import nbp

nbp.DEBUG = True

text = nbp.get_tables(date="2017-12-32")
if text:
  data = json.loads(text)
  print(data[0])
```
Result:
```

```

---

Similar project: https://github.com/jqb/python-nbp


