import unittest

from oops.person import Male, Female, Person
class TestPerson(unittest.TestCase):
    def test_male_gender(self):
        male = Male()
        self.assertEqual(male.get_gender(), "Male")

    def test_female_gender(self):
        female = Female()
        self.assertEqual(female.get_gender(), "Female")

    def test_person_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Person()

if __name__ == "__main__":
    unittest.main()