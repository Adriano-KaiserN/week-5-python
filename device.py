# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Device: {self.brand} {self.model}")

# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model}")

# Example usage
phone1 = Smartphone("Apple", "iPhone 14", "iOS", "128GB")
phone1.info()
phone1.make_call("+254742794551")
phone1.install_app("WhatsApp")