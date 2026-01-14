from pythonsdk import sayHello

def test_sayHello():
    assert sayHello() == "hello"
    print("sayHello() returns:", sayHello())

if __name__ == "__main__":
    test_sayHello()

