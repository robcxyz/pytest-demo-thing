import os
import pytest

from canbus_thing.reader import create_canbus_reader, CanbusReader


def test_reader_read_new_thing():
    # Most basic way...
    db_location = os.path.join(os.path.dirname(__file__), 'fixtures', 'snapshot-1.dbc')
    db = create_canbus_reader(db_location)
    msg = db.read()

    assert msg.autosar is None


@pytest.mark.parametrize('db_location', [
    'snapshot-1.dbc',
    'snapshot-2.dbc',
    'snapshot-3.dbc',
])
def test_reader_read_new_thing_parametrize(db_location):
    # This is a more advanced way to do the same thing
    db_location = os.path.join(os.path.dirname(__file__), 'fixtures', db_location)
    db = create_canbus_reader(db_location)
    assert db


@pytest.mark.parametrize('db_location,value,expected_value', [
    ('snapshot-1.dbc', 'autosar', None),
])
def test_reader_read_new_thing_parametrize(db_location, value, expected_value):
    # This is a more advanced way to do the same thing
    db_location = os.path.join(os.path.dirname(__file__), 'fixtures', db_location)
    db = create_canbus_reader(db_location)
    msg = db.read()

    # Some function that is complicated

    value = getattr(msg, value)

    assert value == expected_value


@pytest.fixture
def db_location1():
    return 'snapshot-1.dbc'


def test_reader_with_fixture(db_location1):
    # This is a more advanced way to do the same thing
    db_location = os.path.join(os.path.dirname(__file__), 'fixtures', db_location1)
    db = create_canbus_reader(db_location)
    msg = db.read()

    # Some function that is complicated
    assert msg.autosar is None


@pytest.fixture
def db_location_fixture_getter_thing():
    def f(file):
        return os.path.join(os.path.dirname(__file__), 'fixtures', file)

    return f


def test_reader_with_fixture_func_thing(db_location_fixture_getter_thing):
    # This is a more advanced way to do the same thing
    db_location = db_location_fixture_getter_thing('snapshot-1.dbc')
    db = create_canbus_reader(db_location)
    msg = db.read()

    # Some function that is complicated
    assert msg.autosar is None


@pytest.fixture
def fixtures_dir_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.fixture
def mock_reader(fixtures_dir_path):
    def f(file):
        return create_canbus_reader(os.path.join(fixtures_dir_path, file))

    return f


# From conftest file
@pytest.fixture
def mock_reader_2(fixtures_dir_path_2):
    def f(file):
        return create_canbus_reader(os.path.join(fixtures_dir_path_2, file))

    return f


def test_reader_with_fixture_func_thing_2(mock_reader):
    # This is a more advanced way to do the same thing
    db = mock_reader('snapshot-1.dbc')
    msg = db.read()

    # Some function that is complicated
    assert msg.autosar is None


def test_reader_curdir(mocker, mock_reader):
    mocker.patch('canbus_thing.reader.os.getcwd', return_value='test_foo')
    db = mock_reader('snapshot-1.dbc')

    assert db.get_path() == 'test_foo'
