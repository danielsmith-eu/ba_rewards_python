# BA Rewards

This is a port of @timrogers [https://github.com/timrogers/ba_rewards](BA Rewards)ruby gem to python, and a command-line client to access it via cron etc.

## Setup

Recommended: Use virtualenv and install requirements using pip:

    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

Then run the app:

    python app.py


For more information on arguments: `python app.py --help`


    usage: app.py [-h] [--class CLASS] [--number NUMBER] from to

    Look up oneworld award flight availability via Avios.com.

    positional arguments:
      from             Departure Airport (3-letter CITY Code, e.g. LON, not LHR)
      to               Arrival Airport (3-letter CITY Code, e.g. PAR, not CDG)

    optional arguments:
      -h, --help       show this help message and exit
      --class CLASS    Class of travel: economy, premium, business, first
      --number NUMBER  Number of seats required

E.g.:

    python app.py LON EDI --class=business --number=2

