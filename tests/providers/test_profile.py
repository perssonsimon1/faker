import unittest

from faker import Faker


class TestEnUS(unittest.TestCase):
    """ Tests contact_info in the en_USs locale """

    def setUp(self):
        self.fake = Faker('')
        Faker.seed(0)

    def test_contact_info(self):
        res = self.fake.contact_info()

        assert res
        assert isinstance(res, dict)
        assert "address" in res
        assert "name" in res
        assert "phone" in res
        assert isinstance(res['address'], str)
        assert isinstance(res['name'], str)
        assert isinstance(res['phone'], str)
