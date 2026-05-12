from typing import TypedDict, NotRequired, Required

class Order(TypedDict):
   order_id: str
   due: str
   products: NotRequired[list[str]]


Product = TypedDict(
   "Product",
   {
      "product_id": str,
      "quantity": int,
      "operations": NotRequired[list[str]]
   },
   total=False
)

Machine = TypedDict('Machine', {'capacity': int, 'type': Required[str]}, total=True)

def main():
   order: Order = {
      'order_id': "PO1001",
      'due': '20261201',
    }
   print(order)

   product: Product = {
      'product_id': 'p001',
      'quantity': 100,
      'operations': ['op1', 'op2']
   }
   print(product)

   machine: Machine = {
      'capacity': 1000,
      'type': 'etch'
   }
   print(machine)

if __name__ == "__main__":
   main()
