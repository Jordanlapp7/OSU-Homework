# Author: Jordan Lapp
# GitHub username: JordanLapp
# Date: 7/21/2023
# Description: Dictionary of pets with ability to add, remove, read to and from JSON file, and display all species.

import json


class DuplicateNameError(Exception):
    """Error raised with Pet with duplicate name is added to NeighborhoodPets."""
    pass


class Pet:
    """Pet with name, species, and owner."""
    def __init__(self, name, species, owner):
        self._name = name
        self._species = species
        self._owner = owner

    def get_name(self):
        """Returns pet's name."""
        return self._name

    def get_owner(self):
        """Returns pet's owner."""
        return self._owner

    def get_species(self):
        """Returns pet's species."""
        return self._species


class NeighborhoodPets:
    """Dictionary of pets with ability to add, remove, read to and from JSON file, and display all species."""
    def __init__(self):
        self._pets = {}

    def add_pet(self, name, species, owner):
        """Adds pet to dictionary if name is not already taken."""
        for pet_name in self._pets:
            if pet_name == name:
                raise DuplicateNameError
        pet = Pet(name, species, owner)
        pet_name = pet.get_name()
        self._pets[pet_name] = pet

    def delete_pet(self, name):
        """Removes pet from dictionary."""
        del self._pets[name]

    def get_owner(self, name):
        """Returns owner's name."""
        return self._pets[name].get_owner()

    def save_as_json(self, file_name):
        """Saves dictionary of pets to JSON file."""
        with open(file_name, 'w') as outfile:
            all_pets = []
            for name in self._pets:
                pet_traits = []
                species = self._pets[name].get_species()
                owner = self._pets[name].get_owner()
                pet_traits.append(name)
                pet_traits.append(species)
                pet_traits.append(owner)
                all_pets.append(pet_traits)
            json.dump(all_pets, outfile)

    def read_json(self, file_name):
        """Reads JSON file and overwrites pet dictionary."""
        with open(file_name, 'r') as infile:
            all_pets = json.load(infile)
            self._pets = {}
            for pet in all_pets:
                name = pet[0]
                species = pet[1]
                owner = pet[2]
                new_pet = Pet(name, species, owner)
                self._pets[name] = new_pet

    def get_all_species(self):
        """Returns a set of the species of all pets."""
        all_species = set()
        for name in self._pets:
            species = self._pets[name].get_species()
            all_species.add(species)
        return all_species
