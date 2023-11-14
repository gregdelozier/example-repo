from mathstuff import add, sub

def test_add():
    assert add(3,4) == 7
    assert add("hot","dog") == "hotdog"

def test_sub():
    assert sub(7,4) == 3

if __name__ == "__main__":
    test_add()
    test_sub()
    print("done.")