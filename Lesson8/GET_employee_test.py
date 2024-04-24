import pytest
import requests


@pytest.fixture
def auth():
    """Fixture to authenticate and retrieve an access token."""
    login_url = "https://x-clients-be.onrender.com/auth/login"
    login_data = {
        "username": "donatello",
        "password": "does-machines"
    }
    response = requests.post(login_url, json=login_data)
    return response.json()["access_token"]


def test_get_employee(auth):
    """Test to verify that the API returns at least one employee and includes all expected fields."""
    url = "https://x-clients-be.onrender.com/employee"
    headers = {"Authorization": f"Bearer {auth}"}
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    employee_data = response.json()[0]
    assert "id" in employee_data
    assert "name" in employee_data
    assert "email" in employee_data


def test_employee_fields_exist(auth):
    """Test to verify that all required fields exist in the first employee's data returned by the API."""
    url = "https://x-clients-be.onrender.com/employee"
    headers = {"Authorization": f"Bearer {auth}"}
    response = requests.get(url, headers=headers)
    employee_data = response.json()[0]
    
    required_fields = ["id", "name", "email"]
    for field in required_fields:
        assert field in employee_data, f"Field '{field}' is missing"


if __name__ == "__main__":
    pytest.main()

