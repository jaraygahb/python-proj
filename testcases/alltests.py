import unittest
import xmlrunner

def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}


def add_fish_to_aquarium(fish_list):
    if len(fish_list) > 10:
        raise ValueError("A maximum of 10 fish can be added to the aquarium")
    return {"tank_a": fish_list}	
	

class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["shark", "tuna"]}
        self.assertEqual(actual, expected)
		

class FishTank:
    def __init__(self):
        self.has_water = False

    def fill_with_water(self):
        self.has_water = True

class TestFishTank(unittest.TestCase):
    def setUp(self):
        self.fish_tank = FishTank()

    def test_fish_tank_empty_by_default(self):
        self.assertFalse(self.fish_tank.has_water)

    def test_fish_tank_can_be_filled(self):
        self.fish_tank.fill_with_water()
        self.assertTrue(self.fish_tank.has_water)
		

class TestAddFishToAquarium(unittest.TestCase):
    def test_add_fish_to_aquarium_success(self):
        actual = add_fish_to_aquarium(fish_list=["shark", "tuna"])
        expected = {"tank_a": ["rabbit"]}
        self.assertEqual(actual, expected)