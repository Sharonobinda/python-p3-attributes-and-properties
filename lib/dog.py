#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unnamed", breed="Mutt"):
        name_error = False
        breed_error = False

        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            name_error = True
        else:
            self.name = name

        if breed not in APPROVED_BREEDS and breed != "Mutt":
            print("Breed must be in list of approved breeds.")
            breed_error = True
        else:
            self.breed = breed

        if name_error:
            self.name = None
        if breed_error:
            self.breed = None