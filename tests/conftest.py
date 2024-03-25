"""
@author: Miguel Cabrera Ramírez <miguel.cabrera@oohel.net><mdark1001>
@project:
@date: 3/24/24
@description: All fixtures needed for a global behavior in all test, here fixtures are load automatically by pytest.
"""

import pytest
from rentomatic.app import create_app
from rentomatic.flask_settings import TestingConfig


@pytest.yield_fixture(scope="function")
def app():
    """
    Create and configure an instance of the Flask application.
    The fixture has been defined with the scope of  a function, which means that it'll be created
    for each test. To maintain the tests isolated from the another ones.
    """
    return create_app(TestingConfig)
