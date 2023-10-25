print('==== #1 Update the Constructor ================')

class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.age = player_dict['age']
        self.position = player_dict['position']
        self.team = player_dict['team']
    
    def __repr__(self):
        return "< Player: {}, {} y/o, pos: {}, team: {} >".format(self.name, self.age, self.position, self.team)
    
    @classmethod
    def get_team(cls, team_list):
        team = []
        for player_dict in team_list:
            player = cls(player_dict)
            team.append(player)
        print(team)


print('\n==== #2 Create Player Instances ===============')
kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
# print(player_kevin) # ? without __repr__(): <__main__.Player object at 0x1041be010>
print(player_kevin.name) # Kevin Durant
print(player_kevin) # ? with __repr__(): Player: Kevin Durant, 34 y/o, pos: small forward, team: Brooklyn Nets

player_jason = Player(jason)
print(player_jason)

player_kyrie = Player(kyrie)
print(player_kyrie)


print('\n==== #3 Create Player Object from a List ======')
players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    }
]
new_team = []
for player_dictionary in players:
    player = Player(player_dictionary)
    new_team.append(player)
print(new_team)


print('\n==== #4 Create Player Object from a Method ====')
team = Player.get_team(players)