import pytest
from unittest import skip
from src.node import Node


@pytest.fixture
def simple_node1():
    input_json1 = '{"username": "Kaley-Wilderman"}'
    expected_xml1 = '<username>Kaley-Wilderman</username>'
    node1 = Node(input_json1)
    return {"node": node1, "json": input_json1, "xml": expected_xml1}


@pytest.fixture
def simple_node2():
    input_json2 = '{"password": "BlaBla012345"}'
    expected_xml2 = '<password>BlaBla012345</password>'
    node2 = Node(input_json2)
    return {"node": node2, "json": input_json2, "xml": expected_xml2}


@pytest.fixture
def simple_node3():
    input_json3 = '{"price": 54.64}'
    expected_xml3 = '<price>54.64</price>'
    node3 = Node(input_json3)
    return {"node": node3, "json": input_json3, "xml": expected_xml3}


@pytest.fixture
def complex_node1():
    input_json = '{"emails": ["Kiel88@gmail.com", "Javon84@gmail.com"]}'
    expected_xml = '<emails><element>Kiel88@gmail.com</element><element>Javon84@gmail.com</element></emails>'
    node = Node(input_json)
    return {"node": node, "json": input_json, "xml": expected_xml}


@pytest.fixture
def complex_node2():
    input_json = '"{coordinates": {"latitude": 39.0617, "longitude": 64.7887}}'
    expected_xml = '<coordinates><latitude>39.0617</latitude><longitude>64.7887</longitude></coordinates>'
    node = Node(input_json)
    return {"node": node, "json": input_json, "xml": expected_xml}


@pytest.fixture
def complex_node3():
    input_json = '{"authors": {"John": {"works": ["Book1", "Book2"]}, "Jeremy": {"works": ["Book3", "Book4"]}}}'

    expected_xml = (
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
    )
    node = Node(input_json)
    return {"node": node, "json": input_json, "xml": ''.join(expected_xml)}


def test_serialize_simple_node(simple_node1, simple_node2, simple_node3):
    assert simple_node1['node'].convert_to_xml() == simple_node1['xml']
    assert simple_node2['node'].convert_to_xml() == simple_node2['xml']
    assert simple_node3['node'].convert_to_xml() == simple_node3['xml']


def test_serialize_complex_node_with_array(complex_node1):
    assert complex_node1['node'].convert_to_xml() == complex_node1['xml']


def test_serialize_complex_node_with_objects(complex_node2):
    assert complex_node2['node'].convert_to_xml() == complex_node2['xml']


def test_serialize_complex_node(complex_node3):
    assert complex_node3['node'].convert_to_xml() == complex_node3['xml']
