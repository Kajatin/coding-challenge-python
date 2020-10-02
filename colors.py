from argparse import ArgumentParser
from getColor import getColor


class Color(object):
    """ A class to store color information.

    Attributes:
    ----------
    name: str
        Name of the color.
    HEX: str
        Hexadecimal representation of the color.
    RGB: dict
        A dictionary with the R, G, and B values of the color.
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'N/A')
        self.hex = kwargs.get('HEX', 'N/A')
        self.rgb = kwargs.get('RGB', 'N/A')

    def __repr__(self):
        return 'Color: {},\tHEX: {},\tRGB: {}'.format(
            self.name,
            self.hex,
            self.rgb)


def main():
    # set up a simple arg parser
    parser = ArgumentParser(description='Script to display color information.')
    parser.add_argument('order', nargs='+', help='order of colors to be displayed')
    args = parser.parse_args()
    
    # minimal solution, not using classes
    minimal(args.order)
    
    # a solution using class instances
    using_classes(args.order)


def using_classes(order):
    """ Prints color information using class instances.

    Parameters
    ----------
    order: list
        A list of color names, e.g. ['red', 'white'].
    """

    # create a list of class instances for each valid `color`
    colors = [Color(**getColor(color)) for color in order if getColor(color) is not None]
    # print the color information for each class instance
    for color in colors:
        print(color)


def minimal(order):
    """ Prints color information using a lambda function directly.

    Parameters
    ----------
    order: list
        A list of color names, e.g. ['red', 'white'].
    """

    # lambda function to print color information
    color_print = lambda info: print('Color: {},\tHEX: {},\tRGB: {}'.format(
                info.get('name','N/A'),
                info.get('HEX','N/A'),
                info.get('RGB','N/A')))

    # print color information for each valid `color`
    [color_print(getColor(color)) for color in order if getColor(color) is not None]


if __name__ == '__main__':
    main()