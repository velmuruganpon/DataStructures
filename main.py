import common

xs = ['vel', 'vel', 'raj']
findStr = 'vel'

def main(xs:list, findStr : str):
  common.findText(xs,findStr.lower())
  

if __name__ == "__main__":
  main(xs, findStr)

