var: str = "module variable"

def outer():
    var = "outer variable"

    def inner():
        nonlocal var  # get var from outer not module
        print(f"find {var} in inner")
    
    inner()
    print(f"find {var} in outer")

outer()

print(f"find {var} in module")
