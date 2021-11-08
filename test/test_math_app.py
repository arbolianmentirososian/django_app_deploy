import json
from django.test import Client


test_client = Client()


def test_hello():
    response = test_client.get("/hello")
    response_data = response.content
    assert response.status_code == 200
    assert 'Hello, world!' in response_data.decode("utf-8")


def test_add():
    response = test_client.get("/add/50/5")
    json_data = json.loads(response.content)
    assert response.status_code == 200
    assert json_data['num1 + num2'] == 55



def test_subtract():
    response = test_client.get("/subtract/50/5")
    json_data = json.loads(response.content)
    assert response.status_code == 200
    assert json_data['num1 - num2'] == 45


def test_multiply():
    response = test_client.get("/multiply/50/5")
    json_data = json.loads(response.content)
    assert response.status_code == 200
    assert json_data['num1 * num2'] == 250


def test_divide():
    response = test_client.get("/divide/50/5")
    json_data = json.loads(response.content)
    assert response.status_code == 200
    assert json_data['num1 / num2'] == 10


def test_modulo():
    response = test_client.get("/modulo/50/5")
    json_data = json.loads(response.content)
    assert response.status_code == 200
    assert json_data['num1 % num2'] == 0