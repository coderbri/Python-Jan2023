class Pet:
    def __init__( self, name, animal_type, tricks, noise ):
        self.name = name 
        self.animal_type = animal_type 
        self.tricks = tricks 
        self.noise = noise 
        
        self.health = 100 
        self.energy = 50  
    
    def __repr__(self):
        return "<< Pet: {} - Type: {} - Tricks: {} - Noise: \"{}\" >>".format(self.name, self.animal_type, self.tricks, self.noise)
    
    def sleep( self ):
        if self.energy < 25:
            self.energy = min(100, self.energy + 25)
            print(f'{self.name} is sleeping (.zzZ Gained 25 energy).')
        else:
            print(f"{self.name} is already well-rested.")
        return self
    
    def eat( self ):
        if self.energy < 45:
            self.energy = min(50, self.energy + 5)
            # self.health = min(100, self.energy + 10)
            print(f'(=^x^=) {self.name} is eating ( *munch* *munch* ). {self.name} just gained 5 energy and 10 health.')
        else:
            print(f"{self.name} is not hungry right now.")
        return self # will execute with .feed()
        
    def play( self ):
        if self.energy >= 25:
            self.energy = max(0, self.energy - 25)
            # self.health = min(100, self.health + 5)
            print(f'(=^x^=) {self.name} played! {self.name} just used 25 energy.')
        else:
            print(f"!!! {self.name} is too tired/weak to play right now. Try feeding or letting {self.name} sleep.")
        return self
    
    def make_noise( self ): # prints out the pet's sound
        print('(=^x^=) {}: "{}".'.format(self.name, self.noise))
        return self
