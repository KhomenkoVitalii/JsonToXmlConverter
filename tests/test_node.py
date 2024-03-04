import pytest
from src.json_to_xml_converter import JSONtoXMLConverter


@pytest.fixture
def simple_username_node():
    input_json = {"username": "Kaley-Wilderman"}
    expected_xml = ['<username>Kaley-Wilderman</username>']
    node = JSONtoXMLConverter(input_json)
    return {"node": node, "json": input_json, "xml": expected_xml}


@pytest.fixture
def simple_password_node():
    input_json = {"password": "BlaBla012345"}
    expected_xml = ['<password>BlaBla012345</password>']
    node = JSONtoXMLConverter(input_json)
    return {"node": node, "json": input_json, "xml": expected_xml}


@pytest.fixture
def simple_numeric_node():
    input_json = {"price": 54.64}
    expected_xml = ['<price>54.64</price>']
    node = JSONtoXMLConverter(input_json)
    return {"node": node, "json": input_json, "xml": expected_xml}


@pytest.fixture
def complex_emails_node():
    input_json = {"emails": ["Kiel88@gmail.com", "Javon84@gmail.com"]}
    expected_xml = [
        '<emails>',
        '<element>Kiel88@gmail.com</element>',
        '<element>Javon84@gmail.com</element>',
        '</emails>'
    ]
    node = JSONtoXMLConverter(input_json)
    return {"node": node, "json": input_json, "xml": expected_xml}


@pytest.fixture
def complex_coordinates_node():
    input_json = {"coordinates": {"latitude": 39.0617, "longitude": 64.7887}}
    expected_xml = [
        '<coordinates>',
        '<latitude>39.0617</latitude>',
        '<longitude>64.7887</longitude>',
        '</coordinates>'
    ]
    node = JSONtoXMLConverter(input_json)
    return {"node": node, "json": input_json, "xml": expected_xml}


@pytest.fixture
def complex_node():
    input_json = {"authors": {"John": {
        "works": ["Book1", "Book2"]}, "Jeremy": {"works": ["Book3", "Book4"]}}}
    expected_xml = [
        '<authors>',
        '<John>',
        '<works>',
        '<element>Book1</element>',
        '<element>Book2</element>',
        '</works>',
        '</John>',
        '<Jeremy>',
        '<works>',
        '<element>Book3</element>',
        '<element>Book4</element>',
        '</works>',
        '</Jeremy>',
        '</authors>'
    ]
    node = JSONtoXMLConverter(input_json)
    return {"node": node, "json": input_json, "xml": expected_xml}


def test_serialize_simple_node(simple_username_node, simple_password_node, simple_numeric_node):
    res = simple_username_node['node'].convert_to_xml(is_string_expected=True)
    for expected in simple_username_node['xml']:
        assert expected in res

    res = simple_password_node['node'].convert_to_xml(is_string_expected=True)
    for expected in simple_password_node['xml']:
        assert expected in res

    res = simple_numeric_node['node'].convert_to_xml(is_string_expected=True)
    for expected in simple_numeric_node['xml']:
        assert expected in res


def test_serialize_complex_node_with_array(complex_emails_node):
    res = complex_emails_node['node'].convert_to_xml(is_string_expected=True)
    for expected in complex_emails_node['xml']:
        assert expected in res


def test_serialize_complex_node_with_objects(complex_coordinates_node):
    res = complex_coordinates_node['node'].convert_to_xml(
        is_string_expected=True)
    for expected in complex_coordinates_node['xml']:
        assert expected in res


def test_serialize_complex_node(complex_node):
    res = complex_node['node'].convert_to_xml(is_string_expected=True)
    for expected in complex_node['xml']:
        assert expected in res
