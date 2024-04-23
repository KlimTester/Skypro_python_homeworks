import pytest
import requests


@pytest.fixture
def auth():
    """Authenticate and return an access token."""
    login_url = "https://x-clients-be.onrender.com/auth/login"
    login_data = {
        "username": "donatello",
        "password": "does-machines"
    }
    response = requests.post(login_url, json=login_data)
    return response.json()["access_token"]


def test_update_employee(auth):
    """Test the employee update functionality."""
    employee_id = 1
    url = f"https://x-clients-be.onrender.com/employee/{employee_id}"
    headers = {"Authorization": f"Bearer {auth}"}
    updated_employee_data = {
        "name": "Updated ilia",
        "email": "updated.klimov888ily@gmail.com",
    }
    response = requests.post(url, json=updated_employee_data, headers=headers)

    assert response.status_code == 200
    response_data = response.json()
    assert "id" in response_data
    assert "name" in response_data
    assert "email" in response_data


def test_required_fields_for_employee_update(auth):
    """Test validation for missing required fields in employee update."""
    employee_id = 1
    url = f"https://x-clients-be.onrender.com/employee/{employee_id}"
    headers = {"Authorization": f"Bearer {auth}"}
    updated_employee_data = {}
    response = requests.post(url, json=updated_employee_data, headers=headers)

    assert response.status_code == 422
    error_details = response.json()
    assert "errors" in error_details
    assert "name" in error_details["errors"]
    assert "email" in error_details["errors"]


if __name__ == "__main__":
    pytest.main()


