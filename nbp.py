#!/usr/bin/env python3

'''
http://api.nbp.pl/
'''

import urllib.request
import json

def get_tables(table='a', format_='json', today=False, date=None, last=None, from_date=None, to_date=None, show_url=False):
    _url = 'http://api.nbp.pl/api/exchangerates/tables/{table}/{args}?format={format}'

    if today:
        args = 'today'
    elif date:
        args = date
    elif last:
        args = 'last/{}'.format(last)
    elif from_date and to_date:
        args = '{}/{}'.format(from_date, to_date)
    else:
        args = ''

    url = _url.format(table=table, args=args, format=format_)

    if show_url:
        print(url)

    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        return None

    return response.read().decode('utf-8')

# -----------------------------------
def get_rates(table='a', code='PLN', format_='json', today=False, date=None, last=None, from_date=None, to_date=None, show_url=False):
    _url = 'http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{args}?format={format}'

    if today:
        args = 'today'
    elif date:
        args = date
    elif last:
        args = 'last/{}'.format(last)
    elif from_date and to_date:
        args = '{}/{}'.format(from_date, to_date)
    else:
        args = ''

    url = _url.format(table=table, code=code, args=args, format=format_)

    if show_url:
        print(url)

    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        return None

    return response.read().decode('utf-8')

# -----------------------------------

def display_table(data):
    print('table:', data['table'])
    print('no:', data['no'])
    print('effectiveDate:', data['effectiveDate'])

    for x in data['rates']:
        print('{} | {:-10s} | {}'.format(x['code'], x['mid'], x['currency']))

def display_table_c(data):
    print('table:', data['table'])
    print('no:', data['no'])
    print('effectiveDate:', data['effectiveDate'])

    for x in data['rates']:
        print('{} | {:-10s} | {:-10s} | {}'.format(x['code'], x['mid'], x['currency']))

# -----------------------------------

def display_rate(data):
    print('table:', data['table'])
    print('currency:', data['currency'])
    print('code:', data['code'])

    for x in data['rates']:
        print('| {} | {} | {:-10s} |'.format(x['no'], x['effectiveDate'], x['mid']))

def display_rate_c(data):
    print('table:', data['table'])
    print('currency:', data['currency'])
    print('code:', data['code'])

    for x in data['rates']:
        print('| {} | {} | {:10s} | {:10s} |'.format(x['no'], x['effectiveDate'], str(x['ask']), str(x['bid'])))

# -----------------------------------

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Get data from NBP',
        epilog='Date format: YYYY-MM-DD\n\nSome arguments may return no data',
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument('-t', metavar='TABLE', type=str, help='table name: A, B or C (default: A)', default='A', dest='table')
    parser.add_argument('-c', metavar='CODE', type=str, help='code (default: PLN)', dest='code')
    parser.add_argument('-d', metavar='DATE', type=str, help='get table for date DATE', dest='date')
    parser.add_argument('-l', metavar='NUMBER', type=int, help='get last NUMBER tables', dest='last')
    parser.add_argument('--today', action='store_true', help='get table for exactly today')
    parser.add_argument('--from', type=str, help='get tables for dates from FROM to TO', dest='from_date')
    parser.add_argument('--to', type=str, help='get tables for dates from FROM to TO', dest='to_date')
    parser.add_argument('--debug', action='store_true', help='show arguments')
    parser.add_argument('--json', action='store_true', help='return json')
    parser.add_argument('--xml', action='store_true', help='return xml')
    parser.add_argument('--url', action='store_true', help='show url')

    args = parser.parse_args()

    if args.debug:
        print('[debug] -t:', args.table)
        print('[debug] -c:', args.code)
        print('[debug] -d:', args.date)
        print('[debug] -l:', args.last)
        print('[debug] --today:', args.today)
        print('[debug] --from:', args.from_date)
        print('[debug] --to:', args.to_date)

    if args.table:
        args.table = args.table.upper()
        if args.table not in ('A', 'B', 'C'):
            print('-t: TABLE has to be A, B or C')
            exit(1)

    if args.last:
        if args.last < 1:
            print('-l: NUMBER hast to be bigger than 0')
            exit(1)

    if args.xml:
        format_ = 'xml'
    else:
        format_ = 'json'

    if args.code:
        text = get_rates(
                table=args.table,
                code=args.code,
                today=args.today,
                date=args.date,
                last=args.last,
                from_date=args.from_date,
                to_date=args.to_date,
                show_url=args.url,
                format_=format_,
            )

        if not text:
            print('No data')
        elif args.json or args.xml:
            print(text)
        else:
            data = json.loads(text)
            if args.table == 'C':
                display_rate_c(data)
            else:
                display_rate(data)

    else:
        #if args.d or args.today or args.l:
        text = get_tables(
                table=args.table,
                today=args.today,
                date=args.date,
                last=args.last,
                from_date=args.from_date,
                to_date=args.to_date,
                show_url=args.url,
                format_=format_,
            )

        if not text:
            print('No data')
        elif args.json or args.xml:
            print(text)
        else:
            data = json.loads(text)
            for x in data:
                if args.table == 'C':
                    display_table_c(x)
                else:
                    display_table(x)
