import argparse
from barewards import BARewards

parser = argparse.ArgumentParser(description='Look up oneworld award flight availability via Avios.com.')
parser.add_argument('from', type=str, action="store", help='Departure Airport (3-letter CITY Code, e.g. LON, not LHR)')
parser.add_argument('to', type=str, action="store", help='Arrival Airport (3-letter CITY Code, e.g. PAR, not CDG)')
parser.add_argument('--class', type=str, action="store", help='Class of travel: economy, premium, business, first', default='economy')
parser.add_argument('--number', type=str, action="store", help='Number of seats required', default='1')

args = vars(parser.parse_args())

ba = BARewards()
print ba.availability(args['from'], args['to'], args['class'], args['number'])



