def add(x: float, y: float):
    return x + y

def do_add():
    return add('4','3')

def test_do_add():
    assert add('4','3') == '43'

if __name__ == '__main__':
    do_add()

