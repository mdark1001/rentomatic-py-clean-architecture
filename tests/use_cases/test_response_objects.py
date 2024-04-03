"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/25/24
"""
import pytest
from rentomatic.request_objects.response_objects import ResponseSuccess


@pytest.fixture
def response_value():
    return {'key': ['value1', 'value2']}


@pytest.fixture
def response_type():
    return 'ResponseError'


@pytest.fixture
def response_message():
    return 'This is a response error'


def test_response_success_is_true(response_value):
    assert bool(ResponseSuccess(response_value)) is True


def test_response_success_has_type_and_value(response_value):
    response = ResponseSuccess(response_value)
    assert response.type == ResponseSuccess.SUCCESS
    assert response.value == response_value
