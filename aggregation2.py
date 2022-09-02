from abc import ABC, abstractmethod


class SoccerAbstract(ABC):
    pass


class Team(ABC):  # Team <-> Player bağ zayıf o yüzden Aggregation
    def __init__(self, team_name, team_value):
        self.team_name = team_name
        self.team_value = team_value
        self.player = None

    def add_player(self, player):
        self.player: Player = player  # Tanımladğım self player : Player classı cinsinden

    def __repr__(self):
        return f'Team Name: {self.team_name}  Team Value: {str(self.team_value)}\n{self.player} '


class Player(ABC):

    def __init__(self, player_name, player_age, player_value, status):
        self.player_name = player_name
        self.player_age = player_age
        self.player_value = player_value
        self.status = status

    def player_property(self):
        if not self.status:
            self.status = f'Not active player'

        else:
            self.status = f'Active Player'

    def __repr__(self):
        return f'Name: {self.player_name} Age: {str(self.player_age)} Value: {str(self.player_value)} Status: {self.status}'
        # PURPOSE |


# Takıma Oyuncu ekleme
# Oyuncuyu ve oynadığı takımı göstermek
# Yaş 40'dan büyükse --> Antrenor sayılsın başında Ant
# -> değilse Ft yazsın
t1 = Team('Galatasaray', 176)
p1 = Player('Mertens', 35, 7, True)
p1.player_property()
t1.add_player(p1)
print(t1)
print(t1.player.player_age)
print(t1.player.player_name)
print(t1.player.player_value)
print(t1.player.status)

print()


class Cripto:
    def __init__(self, company_name, company_date):
        self.company_name = company_name
        self.company_date = company_date
        self.coin = None

    def add_coin(self, coin):
        self.coin: Coin = coin

    def __str__(self):
        return f'{self.company_name} {str(self.company_date)} {str(self.coin)}'


class Coin:
    def __init__(self, coin_name, release_date, value):
        self.coin_name = coin_name
        self.release_date = release_date
        self.value = value

    def __repr__(self):
        return f'{self.coin_name}\n{self.release_date}\n{str(self.value)}'


co1 = Coin('BNB', '2022', 2.40)
cr1 = Cripto('Binance', 2023)
cr1.add_coin(co1)

print(cr1)
