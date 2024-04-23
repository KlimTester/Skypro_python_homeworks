import pytest
import requests

@pytest.fixture
def auth():
    """Fixture to authenticate and return the access token."""
    login_url = "https://x-clients-be.onrender.com/auth/login"
    login_data = {
        "username": "donatello",
        "password": "does-machines"
    }
    response = requests.post(login_url, json=login_data)
    return response.json()["access_token"]

def test_get_employee_by_id(auth):
    """Test to verify that employee details can be fetched by ID."""
    employee_id = 1
    url = f"https://x-clients-be.onrender.com/employee/{employee_id}"
    headers = {"Authorization": f"Bearer {auth}"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    response_json = response.json()
    assert "id" in response_json
    assert "name" in response_json
    assert "email" in response_json

def test_required_fields_for_employee_by_id(auth):
    """Test to verify that all required fields are present in the employee data."""
    employee_id = 1
    url = f"https://x-clients-be.onrender.com/employee/{employee_id}"
    headers = {"Authorization": f"Bearer {auth}"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    response_json = response.json()
    assert "id" in response_json
    assert "name" in response_json
    assert "email" in response_json

if __name__ == "__main__":
    pytest.main()

