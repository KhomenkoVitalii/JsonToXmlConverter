import xml.etree.ElementTree as ET
from xml.dom import minidom


class JSONtoXMLConverter:
    """
    Convert JSON data to XML format.

    Attributes:
        json_data (dict): The JSON data to be converted to XML.
    """

    def __init__(self, json_data: dict):
        self.json_data = json_data

    def convert_to_xml(self, root_name: str = None, is_string_expected: bool = None) -> ET.Element | str:
        """
        Convert JSON data to XML format.

        Args:
            root_name (str, optional): Name for the root element. Defaults to 'root'.
            is_string_expected (bool, optional): Flag to indicate if the output should be returned as a string.
                                                  Defaults to None.

        Returns:
            ET.Element | str: The XML tree or prettified XML string depending on the value of is_string_expected.
        """
        if root_name is None:
            root_name = 'root'

        root = ET.Element(root_name)
        self._create_xml_elements(root, self.json_data)

        if is_string_expected:
            return self.prettify_xml(root)

        return root

    def _create_xml_elements(self, parent: ET.Element, data: dict) -> None:
        """
        Recursively create XML elements based on JSON data.

        Args:
            parent (ET.Element): The parent XML element.
            data (dict): The JSON data to be converted to XML.
        """
        for key, value in sorted(data.items()):
            if isinstance(value, dict):
                sub_element = ET.Element(key)
                parent.append(sub_element)
                self._create_xml_elements(sub_element, value)
            elif isinstance(value, list):
                self._add_list_elements(parent, key, value)
            else:
                element = ET.Element(key)
                element.text = str(value)
                parent.append(element)

    def _add_list_elements(self, parent: ET.Element, key: str, values: list) -> None:
        """
        Create XML elements for lists in JSON data.

        Args:
            parent (ET.Element): The parent XML element.
            key (str): The key of the list in the JSON data.
            values (list): The list to be converted to XML.
        """
        list_element = ET.Element(key)
        for val in values:
            if isinstance(val, dict):
                self._create_xml_elements(list_element, val)
            else:
                element = ET.Element('element')
                element.text = str(val)
                list_element.append(element)
        parent.append(list_element)

    @staticmethod
    def prettify_xml(elem: ET.Element) -> str:
        """
        Prettify XML output for better readability.

        Args:
            elem (ET.Element): The XML element to be prettified.

        Returns:
            str: The prettified XML string.
        """
        rough_string = ET.tostring(elem, 'utf-8')
        parsed = minidom.parseString(rough_string)
        return parsed.toprettyxml()
