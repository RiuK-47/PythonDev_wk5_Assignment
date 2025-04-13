class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.apps = []

    def install_app(self, app_name):
        self.apps.append(app_name)
        print(f"Installed {app_name} on {self.brand} {self.model}.")

    def show_apps(self):
        return f"Apps installed: {', '.join(self.apps)}"

# Example of using the class
my_phone = Smartphone("Apple", "iPhone 16", "256GB")
my_phone.install_app("WhatsApp")
print(my_phone.show_apps())