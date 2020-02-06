import sys

if __name__ == '__main__':

    try:
        filename = sys.argv[1]
        initialize_parking(filename=filename)

    except:
        initialize_parking()
