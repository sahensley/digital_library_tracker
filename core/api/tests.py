from rest_framework import status
from rest_framework.test import APITestCase


class CoreApplicationTests(APITestCase):
    fixtures = ["application.yaml"]

    def test_application_list(self):
        response = self.client.get("/api/application/")
        assert response.status_code == status.HTTP_200_OK

    def test_application_detail(self):
        response = self.client.get("/api/application/1/")
        assert response.status_code == status.HTTP_200_OK


class CoreDeveloperTests(APITestCase):
    fixtures = ["developer.yaml"]

    def test_developer_list(self):
        response = self.client.get("/api/developer/")
        assert response.status_code == status.HTTP_200_OK

    def test_developer_detail(self):
        response = self.client.get("/api/developer/1/")
        assert response.status_code == status.HTTP_200_OK


class CorePersonTests(APITestCase):
    fixtures = ["person.yaml"]

    def test_person_list(self):
        response = self.client.get("/api/person/")
        assert response.status_code == status.HTTP_200_OK

    def test_person_detail(self):
        response = self.client.get("/api/person/1/")
        assert response.status_code == status.HTTP_200_OK


class CorePlatformTests(APITestCase):
    fixtures = ["platform.yaml"]

    def test_platform_list(self):
        response = self.client.get("/api/platform/")
        assert response.status_code == status.HTTP_200_OK

    def test_platform_detail(self):
        response = self.client.get("/api/platform/1/")
        assert response.status_code == status.HTTP_200_OK


class CorePublisherTests(APITestCase):
    fixtures = ["publisher.yaml"]

    def test_publisher_list(self):
        response = self.client.get("/api/publisher/")
        assert response.status_code == status.HTTP_200_OK

    def test_publisher_detail(self):
        response = self.client.get("/api/publisher/1/")
        assert response.status_code == status.HTTP_200_OK
