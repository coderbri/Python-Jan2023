from pet import Pet
from ninja import Ninja

bag_of_treats = ['Friskies', 'Temptations', 'Tuna Flakes', 'Churu']
bag_of_pet_food = ['Hill\'s', 'Arcana', 'Royal Canine']

#* Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
neko_chan = Pet('Neko-Chan', 'cat', ['Give Paw', 'Roll Over', 'Catch Mice'], 'meow meow')
jane_doe = Ninja('Jane', 'Doe', neko_chan, bag_of_treats, bag_of_pet_food)
# print(neko_chan)
# print(jane_doe)

#* Have the Ninja feed, play_with_pet, and bathe their pet.
# jane_doe.display_pet_status()
jane_doe.feed().display_pet_status()
jane_doe.play_with_pet().display_pet_status().play_with_pet().display_pet_status().play_with_pet().display_pet_status()
neko_chan.sleep()
jane_doe.display_pet_status().bathe()