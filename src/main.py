import sys


def initialize_parking(filename=None):
    """
    To initialize parking slots
    """

    if filename: # If the filename is given
        
        with open(filename) as f:
            body = f.readlines()
            body = [x.strip() for x in content]

        first_line = body[0].split()
        output = []

        if first_line[0] == 'exit':
            sys.exit()

        elif first_line[0] == 'create_parking_lot':
            parking_lot_new = 



if __name__ == '__main__':

    try:
        filename = sys.argv[1]
        initialize_parking(filename=filename)

    except:
        initialize_parking()
