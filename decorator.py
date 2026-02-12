from functools import wraps

def access(func):
    def wrapper(*args, **kwargs):
        print("accessing...")
        result = func(*args, **kwargs)
        return result
    return wrapper

def login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("logging in...")
        result = func(*args, **kwargs)
        return result
    return wrapper

def setup(username: str, password: str):
    def decorator(func):
        print(f"setting up for user: {username}...")
        isvalid: bool = password == "12345"
        print(f"password is valid? {isvalid}")
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not isvalid:
                print(f"Auth failed for {username}...")
                return None
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def connect_to(*args, **kwargs):
    print("accessing...")
    print(f"connecting to {kwargs}...")

@access
def connect_to_db(db: str):
    print(f"connecting to db: {db}...")

@login
def connect_to_server(server: str):
    print(f"connecting to server: {server}...")

@setup(username="admin", password="p@$$w0rd")
def connect_to_client(client: str):
    print(f"connecting to client: {client}...")

@setup(username="admin", password="12345")
def connect_to_model(model: str):
    print(f"connecting to model: {model}...")

def main():
    connect_to(db="PostgeSQL")
    print(connect_to.__name__)
    connect_to_db(db="PostgreSQL")
    print(connect_to_db.__name__)
    connect_to_server(server="AWS")
    print(connect_to_server.__name__)
    connect_to_client(client="Windows")
    connect_to_model(model="Gemini")
    

if __name__ == "__main__":
    main()