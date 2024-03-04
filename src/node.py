class Node:
    def __init__(self, json_node):
        self.__json_node = json_node

    def convert_to_xml(self, json=None):
        if json is None:
            json = self.__json_node
        #
        parsed_node, tag_name, value = self.__extract_key_value(json)
        #
        if len(parsed_node) == 2:
            if parsed_node[1].startswith("{"):  # Object
                value = self.__parse_object(parsed_node)
            #
            elif parsed_node[1].startswith("["):  # Array
                value = self.__parse_array(parsed_node)
        #
        xml = self.__create_xml_string(tag_name, value)
        #
        return xml

    def __extract_key_value(self, json):
        parsed_node = json.split(': ', 1)
        if len(parsed_node) == 2:
            tag_name = parsed_node[0].strip('"}{')
            value = parsed_node[1].strip('"}{')
            return [parsed_node, tag_name, value]
        return [parsed_node, 'element', parsed_node[0]]

    def __parse_object(self, parsed_node):
        value = ""
        temp = parsed_node[1].strip("{}")

        # Split the string into separate key-value pairs
        nested_objects = [pair.strip() for pair in temp.split('}')]

        for obj in nested_objects:
            obj_parts = obj.split(': ', 1)
            if len(obj_parts) == 2:
                obj_key, obj_value = obj_parts
                obj_tag_name = obj_key.strip('"}{').strip(', "')
                if len(obj_value.split(': ')) > 1:
                    value += self.__create_xml_string(obj_tag_name,
                                                      self.convert_to_xml(obj_value))
                else:
                    value += self.__create_xml_string(obj_tag_name, obj_value)

        return value

    def __parse_array(self, parsed_node):
        temp = parsed_node[1].strip("}{")
        temp = temp.replace("]", "[")
        temp = temp.replace(", ", "[")
        complex_node_list = temp.split("[")
        value = ""
        for i in range(1, len(complex_node_list)):
            node = complex_node_list[i].strip()
            if node != "":
                value += self.convert_to_xml(f'"element": {node}')
        return value

    def __create_xml_string(self, tag_name, value):
        return f'<{tag_name}>{value}</{tag_name}>'
