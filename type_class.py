class Client:
    def pay(self, amount: int):
        print(f"pays {amount}")

print(type(Client))
print(isinstance(Client, type))

class_body: str = """
def pay(self, amount: int):
    print(f'pays {amount}')

def rent(self, amount: int):
    print(f'rents {amount}')
"""

class_dict: dict = {}
exec(class_body, globals(), class_dict)

Customer = type("Customer", (object,), class_dict)

c = Customer()
c.pay(1_000)
c.rent(1_000)