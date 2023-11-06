# Dojo Pets

**Dojo Pets** is a Python object-oriented programming (OOP) project that simulates the care of virtual pets by a ninja. This project allows you to create and interact with pet objects and their caretakers.


### Table of Contents
1. [Purpose](#purpose)
2. [Classes](#classes)
    - [Pet Class](#pet-class)
    - [Ninja Class](#ninja-class)
3. [Modularization](#modularization)

## Purpose

The purpose of this project is to demonstrate OOP concepts in Python by creating two main classes: `Pet` and `Ninja`. The `Pet` class represents a virtual pet with attributes such as name, animal type, tricks, health, and energy. The `Ninja` class represents a ninja who takes care of the pet and provides methods for feeding, playing with, bathing, and displaying the status of the pet.

## Classes

### Pet Class

#### Attributes

- `name`: The name of the pet.
- `animal_type`: The type of animal (e.g., cat, dog).
- `tricks`: A list of tricks the pet can perform.
- `noise`: The sound the pet makes.
- `health`: The health level of the pet, capped at 100.
- `energy`: The energy level of the pet, capped at 50.

#### Methods

- `sleep()`: Increases the pet's energy by 25 if the energy is less than 25.
- `eat()`: Increases the pet's energy by 5 and health by 10 if the energy is less than 45.
- `play()`: Decreases the pet's energy by 25 if the energy is greater than or equal to 25. Also increases the pet's health by 5 if played.
- `make_noise()`: Prints out the sound the pet makes.

### Ninja Class

#### Attributes

- `first_name`: The first name of the ninja.
- `last_name`: The last name of the ninja.
- `pet`: An instance of the `Pet` class, representing the pet the ninja takes care of.
- `treats`: A list of treats the ninja has.
- `pet_food`: A list of pet food the ninja has.

#### Methods

- `play_with_pet()`: Invokes the pet's `play()` method to play with the pet.
- `feed()`: Invokes the pet's `eat()` method to feed the pet if it's hungry and there is pet food available.
- `bathe()`: Invokes the pet's `make_noise()` method to simulate bathing.
- `display_pet_status()`: Displays the pet's health and energy status.

## Modularization

The code for the `Pet` and `Ninja` classes can be modularized into separate files (`pet.py` and `ninja.py`). Importing these classes allows you to create instances of them and interact with the virtual pets and ninjas.

To use modularization, include the following import statements in the `main.py` file:

```python
from pet import Pet
from ninja import Ninja
```

Then, you can create instances of the classes and interact with them as demonstrated in the code within the `main.py` file.

---
<p align="right">Completed: ２０２３年１１月０６日（月）</p>
