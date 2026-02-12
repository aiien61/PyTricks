amount: int = 10

print(f"amount in local: {amount}")

# works in compiling, error in runtime
def payment(flag: bool):
    if flag:
        amount = 20
    print(f"amount in payment: {amount}")


# use global to make runtime unboundlocalerror fixed
# but better not to use 'global'
def paycheck(flag: bool):
    global amount
    if flag:
        amount = 20
    print(f"amount in paycheck: {amount}")

payment(True)
try:
    payment(False)
except UnboundLocalError as exc:
    print(exc)

paycheck(False)
print(f"amount in local: {amount}")