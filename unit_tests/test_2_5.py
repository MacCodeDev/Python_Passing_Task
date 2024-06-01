import pytest
import requests_mock
import xml.etree.ElementTree as TreeElement
from task_2_5 import get_songs_artists 

@pytest.fixture
def m():
    with requests_mock.Mocker() as m:
        yield m

def test_get_songs_artists(m):
    mock_xml_data = """
    <CATALOG>
        <CD>
            <TITLE>Empire Burlesque</TITLE>
            <ARTIST>Bob Dylan</ARTIST>
        </CD>
        <CD>
            <TITLE>Hide your heart</TITLE>
            <ARTIST>Bonnie Tyler</ARTIST>
        </CD>
    </CATALOG>
    """
    m.get('https://www.w3schools.com/xml/cd_catalog.xml', text=mock_xml_data)

    expected_result = [('Bob Dylan', 'Empire Burlesque'), ('Bonnie Tyler', 'Hide your heart')]
    assert get_songs_artists() == expected_result