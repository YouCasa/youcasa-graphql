from django.contrib.auth import get_user_model
from django.test import TestCase

from rental.models import LGA, Agent, Apartment, City, Country, Landlord, State

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
        self.assertEqual(agent_user.email, "agent@email.com")
        self.assertFalse(agent.can_change_price)
        self.assertFalse(agent.can_change_vacancy)

    def test_create_apartment(self):
        User = get_user_model()
        landlord_user = User.objects.create(email="landlord@email.com", password="foo")
        landlord: Landlord = Landlord.objects.create(user=landlord_user)
        agent_user = User.objects.create(email="agent@email.com", password="foo")
        agent: Agent = Agent.objects.create(user=agent_user)
        country: Country = Country.objects.create(name="MyCountry")
        state:State = State.objects.create(name="MyState")
        lga:LGA = LGA.objects.create(name="MyLGA")
        city:City = City.objects.create(name="MyCity")
        apartment: Apartment = Apartment.objects.create(
            country=country, state=state, lga=lga, city=city,
            address="No. 1 MyAddress street, Silicon Valley",
            description="My test address",
            price=3000.00,
            landlord=landlord,
            price_is_negotiable=True,
            number_of_rooms=3,
            is_vacant=True,
            agent=agent
        )
        self.assertEqual(apartment.country, country)
        self.assertEqual(apartment.state, state)
        self.assertEqual(apartment.lga, lga)
        self.assertEqual(apartment.city, city)
        self.assertEqual(apartment.address, "No. 1 MyAddress street, Silicon Valley")
        self.assertEqual(apartment.description, "My test address")
        self.assertEqual(apartment.price, 3000.00)
        self.assertEqual(apartment.landlord, landlord)
        self.assertEqual(apartment.agent, agent)
        self.assertEqual(apartment.number_of_rooms, 3)
        self.assertTrue(apartment.price_is_negotiable)
        self.assertTrue(apartment.is_vacant)
