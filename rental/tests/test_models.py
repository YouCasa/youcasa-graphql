from django.contrib.auth import get_user_model
from django.test import TestCase

from rental.models import LGA, Agent, City, Country, Landlord, State

class TestRentalModels(TestCase):
    """
    Curretnly tests only creation of rental models.
    """
    def test_create_country_state_lga_and_city(self):
        country:Country = Country.objects.create(name="MyCountry")
        state:State = State.objects.create(name="MyState")
        lga:LGA = LGA.objects.create(name="MyLGA")
        city:City = City.objects.create(name="MyCity")
        self.assertEqual(country.name, "MyCountry")
        self.assertEqual(state.name, "MyState")
        self.assertEqual(lga.name, "MyLGA")
        self.assertEqual(city.name, "MyCity")


    def test_create_landlord_and_agent(self):
        User = get_user_model()
        landlord_user = User.objects.create(email="landlord@email.com", password="foo")
        landlord: Landlord = Landlord.objects.create(user=landlord_user)
        self.assertEqual(landlord_user.email, "landlord@email.com")
        self.assertFalse(not landlord.can_change_price)
        self.assertFalse(not landlord.can_change_vacancy)
        agent_user = User.objects.create(email="agent@email.com", password="foo")
        agent: Agent = Agent.objects.create(user=agent_user)
