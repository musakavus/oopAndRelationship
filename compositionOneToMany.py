# COMPOSİTİON
# ONE TO MANY RELATİON
# HAS A İLİŞKİ VARDIR

from abc import ABC, abstractmethod


class BlokChain(ABC):
    def create_coin(self, coin_id, name): pass

    def add_coin(self): pass


class Binance(BlokChain):
    def __init__(self, name, year):
        self.coin = None
        self.name = name
        self.year = year

    def add_coin(self):
        self.coin = Coin()

    def __str__(self):
        return f'{self.name} {str(self.year)} \n{self.coin}'


class Coin(BlokChain):

    def __init__(self):
        self.coinList = []  # Liste şeklinde ekleme yapıldı

    def create_coin(self, coin_id, name):
        self.coinList.append({coin_id, name})

    def __str__(self):
        return f'{str(self.coinList)}'


b1 = Binance('Binance', 2013)
b1.add_coin()
b1.coin.create_coin(2022, 'ENS')
b1.coin.create_coin(2019, 'DOGE')
print(b1)
