class Player:
    def __init__(self, name , character_class):
        self.name = name
        self.character_class =  character_class

player_1 = Player("Gurgen", "Master") 
player_2 = Player("Ashot", "Master")

print(player_1.name)
print(player_2.name)
