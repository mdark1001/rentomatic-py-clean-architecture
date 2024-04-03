"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/25/24
"""
import pytest
from rentomatic.request_objects.response_objects import ResponseSuccess, ResponseFailure, InvalidRequestObject


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
    res = ResponseSuccess(response_value)
    assert res.type == ResponseSuccess.SUCCESS
    assert res.value == response_value


def test_response_failure_is_false(response_type, response_message):
    assert bool(ResponseFailure(response_type, response_message)) is False


def test_response_failure_has_type_and_messages(response_type, response_message):
    response = ResponseFailure(response_type, response_message)
    assert response.type == response_type
    assert response.message == response_message


def test_response_failure_contains_value(response_type, response_message):
    response = ResponseFailure(response_type, response_message)
    assert response.value == {'type': response_type, 'message': response_message}
def test_response_failure_initialisation_with_exception(response_type):
    response = ResponseFailure(response_type, Exception('Just an error message'))
    assert bool(response) is False
    assert response.type == response_type
    assert response.message == "Exception: Just an error message"

def test_response_failure_from_empty_invalid_request_object():
    response = ResponseFailure.build_from_invalid_request(
        InvalidRequestObject()
    )
    assert bool(response) is False
    assert response.type == ResponseFailure.PARAMETERS_ERROR

def test_response_failure_from_invalid_request_object_with_errors():
    response_object = InvalidRequestObject()
    response_object.add_error('path','Is mandatory')
    response_object.add_error('path', 'cannot be empty')
    response = ResponseFailure.build_from_invalid_request(response_object)
    assert bool(response) is False
    assert response.type == ResponseFailure.PARAMETERS_ERROR
    assert response.message == "path: Is mandatory\npath: cannot be empty"

def test_response_failure_build_resource_error():
    response = ResponseFailure.build_resource_error('test message')
    assert bool(response) is False
    assert response.type == ResponseFailure.RESOURCE_ERROR
    assert response.message == "test message"

def test_response_failure_build_parameters_error():
    response = ResponseFailure.build_parameters_error("test message")
    assert bool(response) is False
    assert response.type == ResponseFailure.PARAMETERS_ERROR
    assert response.message == "test message"

def test_response_failure_build_system_error():
    response = ResponseFailure.build_system_error("test message")
    assert bool(response) is False
    assert response.type == ResponseFailure.SYSTEM_ERROR
    assert response.message == "test message"
