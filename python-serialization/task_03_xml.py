import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to the given filename.

    Parameters:
    dictionary (dict): The Python dictionary to serialize.
    filename (str): The filename to save the serialized XML data.
    """
    root = ET.Element("data")
    
    def build_tree(element, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(element, key)
                build_tree(child, value)
        else:
            element.text = str(data)
    
    build_tree(root, dictionary)
    
    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        return True
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")
        return False

def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file and returns a Python dictionary.

    Parameters:
    filename (str): The filename of the XML file to read and deserialize.

    Returns:
    dict: The deserialized Python dictionary.
    """
    def parse_element(element):
        children = list(element)
        if len(children) == 0:
            return element.text
        result = {}
        for child in children:
            result[child.tag] = parse_element(child)
        return result

    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return parse_element(root)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except ET.ParseError:
        print(f"Error: The file {filename} could not be parsed.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    data = {
        "name": "Alice",
        "age": 30,
        "is_student": True,
        "address": {
            "city": "Wonderland",
            "postal_code": "12345"
        }
    }

    filename = "data.xml"
    
    # Serialize the dictionary to an XML file
    if serialize_to_xml(data, filename):
        print("Data was successfully serialized to XML.")
    else:
        print("Data serialization to XML failed.")
    
    # Deserialize the XML file back to a dictionary
    loaded_data = deserialize_from_xml(filename)
    if loaded_data is not None:
        print("Data was successfully deserialized from XML.")
        print(loaded_data)
    else:
        print("Data deserialization from XML failed.")

