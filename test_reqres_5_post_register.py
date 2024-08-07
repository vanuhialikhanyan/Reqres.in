import pytest
import requests
import allure


@allure.feature("User Registration")
@allure.suite("Register Successfull")
@allure.title("Successful registration with valid credentials")
@allure.description("This test case registers a new user with valid credentials and verifies the response.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_register_successful():
    data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://reqres.in/api/register',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response_data has required fields: id, token'):
        assert 'id' in response_data, "The response does not contain 'id'"
        assert 'token' in response_data, "The response does not contain 'token'"


@allure.feature("User Registration")
@allure.suite("Register Unsuccessfull")
@allure.title("Unsuccessful registration with missing password")
@allure.description("Test case registers a new user without password and verifies that response status code is 400.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_reqres_register_unsuccessfull():
    data = {
        "email": "sydney@fife"
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://reqres.in/api/register',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 400'):
        assert response.status_code == 400, f'Expected Status Code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response_data has "error"'):
        assert 'error' in response_data, "The response does not contain 'error'"
