import pytest
import requests
import allure


@allure.feature("User Management")
@allure.suite("Update Single User")
@allure.title("Update a user with PUT and verify response")
@allure.description("This test case updates an existing user with PUT method and verifies the response.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_reqres_update_user_put():
    user_id = 2
    data = {
         "name": "morpheus",
         "job": "zion resident"
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://reqres.in/api/users/{user_id}',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response_data has required fields: name, job, updatedAt'):
        assert 'name' in response_data, "The response does not contain 'name'"
        assert 'job' in response_data, "The response does not contain 'job'"
        assert 'updatedAt' in response_data, "The response does not contain 'updatedAt'"

    with allure.step('Printing Response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)

@allure.feature("User Management")
@allure.suite("Update Single User")
@allure.title("Update a user with PATCH and verify response")
@allure.description("This test case updates an existing user's information with PATCH method and verifies the response.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_reqres_update_user_patch():
    user_id = 2
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://reqres.in/api/users/{user_id}',
        json=data,
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response_data has required fields: name, job, updatedAt'):
        assert 'name' in response_data, "The response does not contain 'name'"
        assert 'job' in response_data, "The response does not contain 'job'"
        assert 'updatedAt' in response_data, "The response does not contain 'updatedAt'"

    with allure.step('Printing Response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)