from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Companie

# Used ChatGPT to help modify sample test code
class CompanieTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_companie = Companie.objects.create(
            name="Lockheed Martin",
            owner=testuser1,
            description="Aerospace",
        )
        test_companie.save()

    def test_companies_model(self):
        companie = Companie.objects.get(id=1)
        actual_owner = str(companie.owner)
        actual_name = str(companie.name)
        actual_description = str(companie.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Lockheed Martin")
        self.assertEqual(
            actual_description, "Aerospace"
        )

    def test_get_company_list(self):
        url = reverse("company_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        companies = response.data
        self.assertEqual(len(companies), 1)
        self.assertEqual(companies[0]["name"], "Lockheed Martin")

    def test_get_companie_by_id(self):
        url = reverse("company_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        companie = response.data
        self.assertEqual(companie["name"], "Lockheed Martin")

    def test_create_company(self):
        url = reverse("company_list")
        data = {"owner": 1, "name": "General Atmoics",
                "description": "energy"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        companies = Companie.objects.all()
        self.assertEqual(len(companies), 2)
        self.assertEqual(Companie.objects.get(id=2).name,
                         "General Atmoics")

    def test_update_companie(self):
        url = reverse("company_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "Northrop Grumman",
            "description": "Aerospace and defense",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        companie = Companie.objects.get(id=1)
        self.assertEqual(companie.name, data["name"])
        self.assertEqual(companie.owner.id, data["owner"])
        self.assertEqual(companie.description, data["description"])

    def test_delete_companie(self):
        url = reverse("company_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        companies = Companie.objects.all()
        self.assertEqual(len(companies), 0)
