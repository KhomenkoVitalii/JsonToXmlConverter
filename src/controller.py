import json
from src.json_to_xml_converter import JSONtoXMLConverter


class Controller:
    """
    Controller class to manage JSON to XML conversion process.

    Methods:
        start(file_name: str, root_name: str = None) -> None:
            Start the conversion process from JSON file to XML.

    Attributes:
        None
    """

    @staticmethod
    def start(file_name: str, root_name: str = None) -> None:
        """
        Start the conversion process from JSON file to XML.

        Args:
            file_name (str): The name of the JSON file to be converted.
            root_name (str, optional): Name for the root element in the XML. Defaults to None.
        """
        try:
            with open(file_name, 'r') as file:
                json_content = json.load(file)

            converter = JSONtoXMLConverter(json_content)
            xml = converter.convert_to_xml(root_name, is_string_expected=True)

            with open('output.xml', 'w') as xml_file:
                xml_file.write(xml)

        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
