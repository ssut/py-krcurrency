""":mod:`krcurrency.constants` --- Constants for krcurrency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from enum import Enum

class CurrencyCode(Enum):
    USD = 'USA'
    JPY = 'Japan'
    EUR = 'EU'
    GBP = 'England'
    CAD = 'Canada'
    CHF = 'Swiss'
    HKD = 'Hongkong'
    CNY = 'China'
    THB = 'Thailand'
    IDR = 'Indonesia'
    SEK = 'Sweden'
    AUD = 'Austraila'
    DKK = 'Denmark'
    NOK = 'Norway'
    SAR = 'Saudi'
    KWD = 'Kuwait'
    BHD = 'Bahrain'
    AED = 'U.A.E'
    SGD = 'Singapore'
    MYR = 'Malaysia'
    NZD = 'NewZealand'
    TWD = 'Taiwan'
    PHP = 'Philippines'
    VND = 'Vietnam'
    PLN = 'Poland'
    RUB = 'Russia'
    ZAR = 'South Africa'
    INR = 'India'
    PKR = 'Pakistan'
    BDT = 'Bangladesh'
    EGP = 'Egypt'
    MXN = 'Mexico'
    BRL = 'Brazil'
    BND = 'Brunei'
    ILS = 'Israel'
    JOD = 'Jordan'
    CZK = 'the Czech Republic'
    MNT = 'Mongolia'
    FJD = 'Fiji'
    KHR = 'Cambodia'
    TRY = 'Turkey'
    HUF = 'Hungary'
    QAR = 'Qatar'
    XAU = 'GOLD 1g'
    XAG = 'SILVER 1g'

    @classmethod
    def ismember(cls, currency):
        """"""
        currency = currency.upper()
        return currency in cls.__members__
