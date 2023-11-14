from mathstuff import add

def test_add():
    assert add(3,4) == 7
    assert add("hot","dog") == "hotdog"

if __name__ == "__main__":
    test_add()
    print("done.")