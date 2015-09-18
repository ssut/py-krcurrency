""":mod:`krcurrency.classes` --- Classes for krcurrency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

class Bank(object):
    """은행 정의 객체"""
    pass

class Currency(object):
    """환율 객체"""
    def __init__(self, bank=None, code, foreign_send, foreign_recv, cash_buy, cash_sell,
                 buy_tc, standard, bok, usd_rate):
        """
        """
        self.bank = bank
        self._code = code

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        pass
