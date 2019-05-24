

def get_data():
    yield 'data'


def main():
    for i in range(0, 10):
        print('asdfasdf {}'.format(i))
    return get_data()


if __name__ == "__main__":
    main()

