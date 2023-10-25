# Basketball Dictionaries

The `Player` class is designed to represent information about basketball players. It has attributes such as `name`, `age`, `position`, and `team`. The objective is to create and manage instances of the `Player` class and demonstrate how to initialize objects from dictionaries.

#### Table of Contents

1. [Update the Constructor](#1-update-the-constructor)
2.  [The `__repr__()` Method](#the-__repr__-method)
3. [Create Player Instances](#2-create-player-instances)
4. [Create Player Objects from a List](#3-create-player-objects-from-a-list)
5. [Create Player Objects from a Method](#4-create-player-objects-from-a-method)

## 1. Update the Constructor

In the initial version of the `Player` class, the constructor accepts individual arguments for the player's attributes. Here's the original constructor:

```python
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
```

In this updated version, the constructor is now set up to accept a single dictionary containing the player's information. This change allows for more flexibility and cleaner code. The modified constructor looks like this:

```python
class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.age = player_dict['age']
        self.position = player_dict['position']
        self.team = player_dict['team']
```


### The `__repr__()` Method

Additionally, the Player class includes a special method called `__repr__()`. This method is designed to provide a string representation of a Player object. The `__repr__()` method generates a custom string with player information that is useful for debugging and displaying the object. For example:

```python
def __repr__(self):
    return "< Player: {}, {} y/o, pos: {}, team: {} >".format(self.name, self.age, self.position, self.team)
```

When you print a Player object, it will display a human-readable string representation like:

```
Player: Kevin Durant, 34 y/o, pos: small forward, team: Brooklyn Nets.
```

In summary, the `__repr__()` method ensures that Player objects are easily identifiable and informative when used in your code.


## 2. Create Player Instances

In this section, instances of the `Player` class are created using dictionaries that represent basketball players. Each player's information is defined as a dictionary with keys like `"name"`, `"age"`, `"position"`, and `"team."`. Here's an example of creating a `Player` instance:

```python
kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
```

## 3. Create Player Objects from a List

In this section, we populate a list of `Player` objects from a list of dictionaries. The objective is to create a `Player` object for each dictionary in the list. Here's the structure of the process:

```python
new_team = []
for player_dictionary in players:
    player = Player(player_dictionary)
    new_team.append(player)
```

We iterate through the `players` list, creating a `Player` object for each player's dictionary, and append the objects to the `new_team` list.


## 4. Create Player Objects from a Method

The final objective is to create a class method called `get_team(cls, team_list)` that, given a list of dictionaries, populates and returns a new list of `Player` objects. Here's how this class method can be used:

```python
# for brevity, the rest of constructor is removed
    # ...
    @classmethod
        def get_team(cls, team_list):
            team = []
            for player_dict in team_list:
                player = cls(player_dict)
                team.append(player)
            print(team)

team = Player.get_team(players)
```

The `get_team()` method is designed to simplify the process of creating a list of `Player` objects from a list of player dictionaries.

These changes and additions make the `Player` class more versatile and efficient when working with basketball player data.

---
<p align="right">Completed: ２０２３年１０月２４日（火）</p>