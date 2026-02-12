def without_currying():
    from typing import Callable
    def multiply_setup(a: int) -> Callable[[int], int]:
        def multiply(b: int) -> int:
            return a * b
        return multiply
    
    double = multiply_setup(2)
    triple = multiply_setup(3)
    
    print(double(10))
    print(triple(10))

def with_currying():
    from functools import partial

    def multiply(a: int, b: int) -> int:
        return a * b
    
    double = partial(multiply, 2)
    triple = partial(multiply, 3)

    print(double(10))
    print(triple(10))

    def greet(name: str, greeting: str = 'Hello'):
        print(f'{greeting}, {name}')

    yo = partial(greet, greeting='Yo')
    hola = partial(greet, greeting='Hola')
    yo('Bob')
    hola('Bob')

def main():
    from typing import Callable

    type FinalPrice = Callable[[float], float]
    type DiscountFactory = Callable[[float], FinalPrice]

    def apply_vat(tax_rate: float) -> DiscountFactory:
        def apply_discount(discount_amount: float) -> FinalPrice:
            def calculate_final(price: float) -> float:
                return (price - discount_amount) * (1 + tax_rate)
            return calculate_final
        return apply_discount
    
    discount: DiscountFactory = apply_vat(0.25)
    apply_black_friday: FinalPrice = discount(300.0)
    apply_christmas: FinalPrice = discount(150.0)
    
    fridge_price: int = 500
    print(f"Fridge: ${fridge_price}")
    print(f"Black friday price: ${apply_black_friday(fridge_price)}")
    print(f"Christmas price: ${apply_christmas(fridge_price)}")

if __name__ == "__main__":
    without_currying()
    with_currying()
    main()
