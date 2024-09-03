class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        if pet_type in Pet.PET_TYPES:
            return None
        else:
            raise Exception


class Owner:


    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        non_list = [pet for pet in Pet.all if pet.owner == self]
        return(sorted(non_list, key=lambda pet: pet.name))