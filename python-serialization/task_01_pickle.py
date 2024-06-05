import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing the object: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"An error occurred while deserializing the object: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    # Creating an instance of CustomObject
    obj = CustomObject("John", 25, True)
    
    # Displaying the object's attributes
    obj.display()
    
    # Serializing the object to a file
    obj.serialize("custom_object.pkl")
    
    # Deserializing the object from the file
    loaded_obj = CustomObject.deserialize("custom_object.pkl")
    
    if loaded_obj:
        # Displaying the deserialized object's attributes
        loaded_obj.display()

