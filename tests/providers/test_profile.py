import unittest

from faker import Faker


class TestEnUS(unittest.TestCase):
    """ Tests contact_info in the en_USs locale """

    def setUp(self):
        self.fake = Faker('')
        Faker.seed(0)

    def test_contact_info_1(self):
        res = self.fake.contact_info()
        print(res)

        assert res
