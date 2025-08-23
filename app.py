def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

if __name__ == "__main__":
    print("App running... 2+3 =", add(2, 3))
