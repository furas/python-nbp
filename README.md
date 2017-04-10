
Exchange rates from NBP (Narodowy Bank Polski - Polish National Bank)

API: http://api.nbp.pl/ (PL), http://api.nbp.pl/en.html (EN)

Examples in CLI

  $ nbp.py -t C -c usd -l 5 --xml --url

  $ python3 -m nbp -t C -c usd -l 5 --xml --url

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

Examples in code

  import nbp

  text = nbp.get_rates(table='C', code='usd', last=5, format='xml', show_url=True)
  print(text)

  text = nbp.get_tables(table='A', code='usd', last=5)
  if text:
    data = json.loads(text)
    print(data[0])
