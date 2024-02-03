import pytest
import os


@pytest.fixture(scope='session', autouse=True)
def fixtures_dir_path_2():
    return os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.fixture
def setup_test():
    # Pointless
    print('setup test')
    yield


@pytest.fixture
def teardown_test():
    yield
    print('teardown test')


@pytest.fixture
def setup_and_teardown():
    print('setup and teardown')
    yield
    print('teardown and setup')