import pytest
import requests
import allure


@allure.feature("User API")
@allure.suite("Get User List")
@allure.title("Get the list of users from page 2")
@allure.description("Test to get the list of users from page 2 and validate the response structure and content.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_reqres_list_users():
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        'https://reqres.in/api/users?page=2',
        headers=headers
    )

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "data" field'):
        assert 'data' in response_data, "The response does not contain 'data'"

    with allure.step('Verify "data" field is a list'):
        assert isinstance(response_data['data'], list), "'data' should be a list"

    with allure.step('Verify the user list is not empty'):
        assert len(response_data['data']) > 0, 'The user list should not be empty'

    with allure.step('Verify each user has required fields: id, email, first_name, last_name, avatar'):
        for user in response_data['data']:
            assert 'id' in user, "User does not contain 'id'"
            assert 'email' in user, "User does not contain 'email'"
            assert 'first_name' in user, "User does not contain 'first_name'"
            assert 'last_name' in user, "User does not contain 'last_name'"
            assert 'avatar' in user, "User does not contain 'avatar'"

    with allure.step('Verify the response contains "support" field'):
        assert 'support' in response_data, "The response does not contain 'support'"

    with allure.step('Verify "support" field contains "url" and "text"'):
        assert 'url' in response_data['support'], "'Support' does not contain 'url'"
        assert 'text' in response_data['support'], "'Support' does not contain 'text'"


@allure.feature("User API")
@allure.suite("Get Single User")
@allure.title("Get details of a single user")
@allure.description('Test to get the details of a single user with ID 2 and validate response status and content.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_reqres_single_user():
    with allure.step('Send GET request to fetch users from page 2'):
        response = requests.get('https://reqres.in/api/users/2')

    with allure.step('Verify the response status code is 200'):
        assert response.status_code == 200, f'Expected status code 200 but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify the response contains "data" field'):
        assert 'data' in response_data, "The response does not contain 'data'"

    user = response_data['data']

    with allure.step('Verify each user has required fields: id, email, first_name, last_name, avatar'):
        assert 'id' in user, "User does not contain 'id'"
        assert 'email' in user, "User does not contain 'email'"
        assert 'first_name' in user, "User does not contain 'first_name'"
        assert 'last_name' in user, "User does not contain 'last_name'"
        assert 'avatar' in user, "User does not contain 'avatar'"

    with allure.step('Verify the response contains "support" field'):
        assert 'support' in response_data, "The response does not contain 'support'"

    with allure.step('Verify "support" field contains "url" and "text"'):
        assert 'url' in response_data['support'], "'Support' does not contain 'url'"
        assert 'text' in response_data['support'], "'Support' does not contain 'text'"


@allure.feature("User API")
@allure.suite("Get Single User Not Found")
@allure.title("Verify that calling a non-existing user returns 404")
@allure.description("Test checks that a request for a user with non-existent ID 23, returns a 404 status code.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_reqres_single_user_not_found():
    with allure.step('Send GET request for a non-existing user with ID 23'):
        response = requests.get('https://reqres.in/api/users/23')

    with allure.step('Verify the response status code is 404'):
        assert response.status_code == 404, f'Expected status code 404 but got {response.status_code}'
