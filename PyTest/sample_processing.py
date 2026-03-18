class OutsideAPI:
    def do_something(self):
        return 'API execution result'

def my_processing():
    api = OutsideAPI()
    return api.do_something() + " returning something"

if __name__ == "__main__":
    print(my_processing())
