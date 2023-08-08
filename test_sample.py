
import pytest
import requests
import json

url = "https://census-toy.nceng.net/prod/toy-census"

def test_api_barcelona_full_team():
    barcelona = requests.post(url)
    assert barcelona.status_code == 200

def test_api_request_full_body():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},{"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},{"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},{"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},{"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},{"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},{"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    returning_data = response.json()
    assert {"name": "male", "value": 40} in returning_data
    assert {"name": "female", "value": 24} in returning_data
    assert {"name": "other", "value": 16} in returning_data
# Test how API responds to the empty body
def test_api_response_empty_body():
    response = requests.post(url)
    assert response.status_code == 400  # Expecting a 400 Bad Request due to missing required fields


# Test if the API returns the correct response for CountByGender action type
def test_count_by_gender():
    data = {
        "actionType": "CountByGender",
        "users": [
            {"gender": "male"},
            {"gender": "female"},
            {"gender": "male"},
            {"gender": "other"},
            {"gender": "other"}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    returning_data = response.json()
    assert {"name": "male", "value": 2} in returning_data
    assert {"name": "female", "value": 1} in returning_data
    assert {"name": "other", "value": 2} in returning_data

    # Test if the API returns the correct response for CountByCountry action type
def test_count_by_country():
    data = {
        "actionType": "CountByCountry",
        "users": [

            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "US"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "CA"},
            {"nat": "FR"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"},
            {"nat": "UK"}
        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()
    assert {"name": "US", "value": 99} in result
    assert {"name": "UK", "value": 693} in result
    assert {"name": "CA", "value": 396} in result
    assert {"name": "FR", "value": 99} in result

    # Test if the API returns the correct response for CountPasswordComplexity action type
def test_count_password_complexity():
    data = {
        "actionType": "CountPasswordComplexity",
        "users": [
            {"login": {"password": ")(*@008"}},# 0 - password complexity
            {"login": {"password": "12345!"}},# 3 - password complexity
            {"login": {"password": "!@#456"}}, # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity
            {"login": {"password": ")(*@008"}},  # 0 - password complexity
            {"login": {"password": "12345!"}},  # 3 - password complexity
            {"login": {"password": "!@#456"}},  # # 3 - password complexity

        ]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    result = response.json()

    assert {"name": ")(*@008", "value": 4} in result
    assert {"name": "12345!", "value": 1} in result
    assert {"name": "!@#456", "value": 3} in result

    actual_result = [
        {'name': ')(*@008', 'value': 4}, ##!!!!! bug
        {'name': '12345!', 'value': 1},  ## !!!!!!Bug
        {'name': '!@#456', 'value': 3}  # true
    ]

