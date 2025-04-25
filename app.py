class Patient:
    def __init__(self, name, age, condition):
        self.name = name
        self.age = age
        self.condition = condition

    def display_info(self):
        return f"Patient: {self.name}, Age: {self.age}, Condition: {self.condition}"

# Sample usage
if __name__ == "__main__":
    patient1 = Patient("John Doe", 45, "Diabetes")
    print(patient1.display_info())
