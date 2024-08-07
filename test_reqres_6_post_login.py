import pytest
import requests
import allure


@allure.feature("User Login")
@allure.story("Login Successfull")
@allure.title("Successful login with valid credentials")
@allure.description("This test case checks user login with valid credentials and verifies the response.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_login_successfull():
    data = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://reqres.in/api/login',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response_data has "token"'):
        assert 'token' in response_data, "The response does not contain 'token'"


@allure.feature("User Login")
@allure.suite("Login Unsuccessfull")
@allure.title("?????")
@allure.description("??????")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_reqres_login_unsuccessfull():
    data = {
    "email": "peter@klaven"
}

    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://reqres.in/api/login',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 400'):
        assert response.status_code == 400, f'Expected Status Code 400, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response_data has "error"'):
        assert 'error' in response_data, "The response does not contain 'error'"