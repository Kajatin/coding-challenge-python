from argparse import ArgumentParser
from getColor import getColor

class Color(object): 
    def __init__(self, name):
            self.name = name
        
class Red(Color): 
  def __init__(self, name):
      Color.__init__(self, "red")
      
class Green(Color): 
  def __init__(self, name):
      Color.__init__(self, "green")

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--green', dest='green', default="")
    parser.add_argument('--blue', dest='blue')
    parser.add_argument('--red', dest='red')
    parser.add_argument('--order', dest='order',  nargs="+", required=True)
    return parser

def main():
    parser = build_parser()
    options = parser.parse_args()
    getColors(
        options.green,
        options.blue,
        options.red,
        options.order,
        output
        )
    
def output(colors):
    hexColors = []
    print(colors)
    for x in colors:
        hexColors.append(x["HEX"])
    print("Red " + hexColors[0])
    print("Green " + hexColors[1])

def getColors(green,blue,red,order,callback):
    colors = []
    if green: colors.insert(order.index("green"),getColor("green"))
    if blue: colors.insert(order.index("blue"),getColor("blue"))
    if red: colors.insert(order.index("red"),getColor("red"))
    callback(colors)
    return colors


if __name__ == '__main__':
    main()
