from common import findListElement

xs = ['vel', 'vel', 'raj']
findStr = 'vel'


def main(xs:list, findStr : str):
  findListElement(xs,findStr.lower())


if __name__ == "__main__":
  main(xs, findStr)

