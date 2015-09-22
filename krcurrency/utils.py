""":mod:`krcurrency.utils` --- Helpers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from bs4 import BeautifulSoup as BS
import requests

__all__ = 'request',

def request(url, encoding='utf-8', parselib='lxml'):
    """url로 요청한 후 돌려받은 값을 BeautifulSoup 객체로 변환해서 반환합니다.


    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    soup = None
    try:
        soup = BeautifulSoup(r.text, parselib)
    except Exception as e:
        pass
    return soup