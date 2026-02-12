from typing import TypedDict, NotRequired

class Order(TypedDict):
   order_id: str
   due: str
   products: NotRequired[list[str]]


Product = TypedDict(
   "Product",
   {
      "product_id": str,
      "quantity": int,
      "jobs": NotRequired[list[str]]
   }
)


def main():
   order: Order = {
      'order_id': "PO1001",
      'due': '20261201',
    }
   print(order)

   product: Product = {
      'product_id': 'p001',
      'quantity': 100,
      'jobs': ['j001', 'j002']
   }
   print(product)

if __name__ == "__main__":
   main()
