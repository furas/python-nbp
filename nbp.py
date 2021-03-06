#!/usr/bin/env python3

'''
Getting data from http://api.nbp.pl/
'''

import urllib.request

DEBUG = False
'''Display request exception'''


def get_tables(table='a', format_='json', today=False, date=None, last=None,
               from_date=None, to_date=None, show_url=False):
    '''
    It gets tables from server and returns as string or None.
    You have to check if it result is not None and then decode to JSON

    table='a'
    format_='json'
    today=False
    date=None
    last=None
    from_date=None
    to_date=None
    show_url=False

    Example:

    text = nbp.get_tables()
    if text:
        data = json.loads(text)
        nbp.display_table(data)
    '''

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
    except urllib.error.HTTPError as ex:
        if DEBUG:
            print('DEBUG: request error:', ex)
        return None

    return response.read().decode('utf-8')


def get_rates(table='a', code='EUR', format_='json', today=False, date=None,
              last=None, from_date=None, to_date=None, show_url=False):
    '''
    It gets rates from server and returns as string or None.
    You have to check if result is not None and then decode to JSON

    Example:

    text = nbp.get_rates()
    if text:
        data = json.loads(text)
        nbp.display_rates(data)
    '''

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
    except urllib.error.HTTPError as e:
        if DEBUG:
            print('DEBUG: request error:', e.decode('utf-8'))
        return None

    return response.read().decode('utf-8')


def display_table(data):
    '''Display table from dictionary `data`'''

    for part in data:

        print('table:', part['table'])
        print('no:', part['no'])
        print('effectiveDate:', part['effectiveDate'])

        if part['table'] == 'C':
            for x in part['rates']:
                print('{} | {:10s} | {:10s} | {}'.format(x['code'], str(x['ask']), str(x['bid']), x['currency']))
        else:
            for x in part['rates']:
                print('{} | {:10s} | {}'.format(x['code'], str(x['mid']), x['currency']))


def display_rates(data):
    '''Display rates from dictionary `data`'''

    print('table:', data['table'])
    print('currency:', data['currency'])
    print('code:', data['code'])

    if data['table'] == 'C':
        for x in data['rates']:
            print('| {} | {} | {:10s} | {:10s} |'.format(x['no'], x['effectiveDate'], str(x['ask']), str(x['bid'])))
    else:
        for x in data['rates']:
            print('| {} | {} | {:10s} |'.format(x['no'], x['effectiveDate'], str(x['mid'])))


if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description='Get data from NBP',
        epilog='Date format: YYYY-MM-DD\n\nSome arguments may return no data',
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument('-t', metavar='TABLE', type=str, help='table name: A, B or C (default: A)', default='A', dest='table')
    parser.add_argument('-c', metavar='CODE', type=str, help='code of currency', dest='code')
    parser.add_argument('-d', metavar='DATE', type=str, help='table for date DATE', dest='date')
    parser.add_argument('-l', metavar='NUMBER', type=int, help='last NUMBER tables', dest='last')
    parser.add_argument('--today', action='store_true', help='table for exactly today')
    parser.add_argument('--from', type=str, help='tables from FROM_DATE to TO_DATE', dest='from_date')
    parser.add_argument('--to', type=str, help='tables from FROM_DATE to TO_DATE', dest='to_date')
    parser.add_argument('--json', action='store_true', help='return json')
    parser.add_argument('--xml', action='store_true', help='return xml')
    parser.add_argument('--url', action='store_true', help='show url')
    parser.add_argument('--debug', action='store_true', help='show arguments')

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
            format_=format_,
            show_url=args.url,
        )

        if not text:
            print('No data')
        elif args.json or args.xml:
            print(text)
        else:
            display_table(json.loads(text))

    else:
        #if args.d or args.today or args.l:
        text = get_tables(
            table=args.table,
            today=args.today,
            date=args.date,
            last=args.last,
            from_date=args.from_date,
            to_date=args.to_date,
            format_=format_,
            show_url=args.url,
        )

        if not text:
            print('No data')
        elif args.json or args.xml:
            print(text)
        else:
            display_table(json.loads(text))
