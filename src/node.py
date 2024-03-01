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

        # if nested obj doesn't contain another obj
        if self.__count_nested_obj(parsed_node[1]) == 1:
            temp = parsed_node[1].strip("{}")
            temp = temp.replace("}", "{")
            temp = temp.replace(", ", "{")
            complex_node_list = temp.split("{", 1)
            print(complex_node_list)
            for i in range(0, len(complex_node_list)):
                node = complex_node_list[i].strip()
                if node != "" and len(node.split(': ', 1)) >= 2:
                    value += self.convert_to_xml(node)
        else:
            # temp = parsed_node[1].split(': ')
            # if len(temp) % 2 == 0:
            #     for i in range(len(temp)):
            #         temp_json = temp[i].join(": ").join(temp[i+1])
            #         temp.pop(i+1)
            #         value += self.convert_to_xml(temp_json)
            # else:
            value += self.convert_to_xml(parsed_node[1])

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

    def __count_nested_obj(self, json):
        num = 0
        for char in json:
            if char == '{':
                num += 1
        return num

    def __create_xml_string(self, tag_name, value):
        return f'<{tag_name}>{value}</{tag_name}>'
