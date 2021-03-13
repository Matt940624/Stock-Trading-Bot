import alpaca_trade_api as tradeapi
import os
from datetime import datetime

os.environ['APCA_API_BASE_URL'] = 'https://paper-api.alpaca.markets'

# API credentials
api = tradeapi.REST('PK8XYB3SLLFYA78HI7DS', '9PLhpUeAo4xDoi3nN4zmAZzW1HXRmJ31TZHax9RG', api_version='v2')
account = api.get_account()


# Check if the market is open now.
clock = api.get_clock()
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

# Check when the market was open on Dec. 1, 2018
date = datetime.now()
calendar = api.get_calendar(start=date, end=date)[0]
print('The market opened at {} and closed at {} on {}.'.format(
    calendar.open,
    calendar.close,
    date
))