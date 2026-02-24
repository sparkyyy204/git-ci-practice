from main import greet

def test_greet():
    assert greet("world") == "Hello, world!"
    print("Тест пройден успешно!")

if __name__ == "__main__":
    test_greet()
