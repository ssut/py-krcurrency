""":mod:`krcurrency.banks.woori` --- 우리은행
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from krcurrency.classes import Bank, Currency
from krcurrency.utils import request, tofloat

class WooriBank(Bank):
    NAME = u'우리은행'
    US_NAME = 'woori bank'
    URL = 'https://spib.wooribank.com/pib/jcc?withyou=ENENG0358&__ID=c008822&BAS_DT='
    KEYS = ['foreign_send', 'foreign_recv', 'cash_buy', 'cash_sell', 'buy_tc', 'standard', 'bok', 'usd_rate']

    def inquiry(self):
        soup = request(WooriBank.URL)
        currencies = {}
        rows = soup.select('table tbody tr')
        for row in rows:
            items = row.select('td')
            code = items[0].text.strip().upper()
            country = items[1].text.strip()
            values = {
                'code': code,
            }
            for i in range(2, 10):
                name = WooriBank.KEYS[i - 2]
                values[name] = tofloat(items[i].text.strip())
            currency = Currency(bank=self, **values)
            currencies[code] = currency

        return currencies
