class Players:
    def __init__(self, name):
        self.name = name


class team:
    def __init__(self):
        self.players = []

    def addPlayers(self, player):
        self.players.append(player)


p = Players("M.S. Dhoni")
t = team()
t.addPlayers(p)
p1 = Players("Sachin")
t.addPlayers(p1)
print(t.players[0].name)
print(t.players[1].name)
del t
# print(t.players[0].name)
print(p.name)
print(p1.name)