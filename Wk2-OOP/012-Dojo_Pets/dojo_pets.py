class Pet:
    def __init__( self, name, animal_type, tricks, noise ):
        self.name = name 
        self.animal_type = animal_type 
        self.tricks = tricks 
        self.noise = noise 
        
        self.health = 100 
        self.energy = 50  
    
    def sleep( self ): # increases the pets energy by 25
        self.energy += 25
        print(f'{self.name} is sleeping (.zzZ Gained 25 energy).')
        return self
    
    def eat( self ): # increases the pet's energy by 5 and health by 10
        self.energy += 5
        self.health += 10
        print(f'(=^x^=) {self.name} is eating ( *munch* *munch* ). {self.name} just gained 5 energy and 10 health.')
        return self # will execute with .feed()
        
    def play( self ): # increases the pet's health by 5
        self.health += 5
        print(f'(=^x^=) {self.name} played! {self.name} just gained 5 health.')
        return self
    
    # ? Naming this as noise() will cause a TypeError as functions and variable can't share the same name, so it is changed to make_noise()
    def make_noise( self ): # prints out the pet's sound
        print('(=^x^=) {}: "{}".'.format(self.name, self.noise))
        return self


class Ninja:
    def __init__( self, first_name, last_name, pet, treats, pet_food ):
        self.first_name = first_name 
        self.last_name = last_name 
        self.pet = pet 
        self.treats = treats
        self.pet_food = pet_food
    
    def walk( self ): # walks the ninja's pet invoking the pet play() method
        print(f'You are playing with {self.pet.name}.')
        self.pet.play()
        print('')
        return self
    
    def feed( self ): # feeds the ninja's pet invoking the pet eat() method
        if len( self.pet_food ) > 0:
            food = self.pet_food.pop()
            print(f'You are feeding {self.pet.name} {food}.')
            self.pet.eat()
            print('')
        else: print("Oh no! You need more pet food!")
        return self
    
    def bathe( self ): # cleans the ninja's pet invoking the pet noise() method
        print(f'You are bathing {self.pet.name}.')
        self.pet.make_noise()
        return self
    
    def display_pet_status( self ):
        print('[ {}\'s Status: {} health, {} energy ]'.format( self.pet.name, self.pet.health, self.pet.energy ))
        return self



my_treats = ['Friskies', 'Temptations', 'Tuna Flakes', 'Churu']
my_pet_food = ['Hills', 'Arcana']

#* Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
neko_chan = Pet('Neko-Chan', 'cat', ['roll over', 'flip', 'mice catch'], 'meow meow')
janedoe = Ninja('Jane', 'Doe', neko_chan, my_treats, my_pet_food,)

#* Have the Ninja feed, walk , and bathe their pet.
janedoe.feed().walk().bathe().display_pet_status()
neko_chan.sleep()

# TODO: NINJA BONUS: Use modules to separate out the classes into different files.
# TODO: SENSEI BONUS: Use Inheritance to create sub classes of pets.
# ? See modularized version for these results.