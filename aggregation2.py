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
