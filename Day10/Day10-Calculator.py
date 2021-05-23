from art import logo

def add(n1, n2):
  return n1 + n2


def sub(n1, n2):
  return n1 - n2


def multi(n1, n2):
  return n1 * n2


def div(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": sub,
  "*": multi,
  "/": div
  }  
def calculator():
  cont = True

  print(logo)

  num1 = float(input("Whats your first number? : \n"))

  for op in operations:
    print(op)

  while cont:
    op_symbol = input("Pick an operation. \n")


    num2 = float(input("Whats your second number? : \n"))


    answer =  operations[f"{op_symbol}"](num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")

    # op_symbol = input("Pick another operation : \n")
    # num3 = int(input("Whats the next number? : \n"))

    # new_answer = operations[f"{op_symbol}"](n1=answer,n2=num3)
    # print(f"{answer} {op_symbol} {num3} = {new_answer}")

    con = input(f"type 'y' to continue calculating with {answer} , or type 'n' to exit : ")
    if con == "n":
      cont = False
      calculator()
    elif con == "y":
      num1 = answer


calculator()
      



