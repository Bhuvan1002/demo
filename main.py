import random

MAX_LINES=3
MAX_BET=100
MIN_BET=10

symbol_count={
    "A":2,
    "B":4,
    "C":6,  
    "D":8
}
 
 ROWS=3
 COLS=3

def get_spin(rows,cols,symbols): # function to get the spin of the slot machine
    all_symbols=[] # empty list to store all the symbols
    for symbol,symbol_count in symbols.items(): #to loop into symbol directory,gives the symbol and count of it #
        for _ in range(symbol_count): # to repeat the symbol based on its count
            all_symbols.append(symbol) # finally the symbol is added to the list all_symbols
    

    columns=[] #defining a col list
    for _ in range(cols): # for creating the number of col
      column=[] # to store val
      current_symbols = all_symbols[:] # to make the copy of all_symbols so that the changes won't affect the org 
    for _ in range(rows):
        value= random .choice(all_symbols) # to randomly choose a symbol from all_symbols list
        current_symbols.remove(value) # to remove the symbol once it is chosen so that it won't be chosen again
        column.append(value) # to add the chosen symbol to the column list

    columns.append(column)
    return columns


def deposit(): # function to get deposit amount
    while True:
         amount=input("enter the amount to be deposited: $")
         if amount.isdigit():
              amount=int(amount)
              if amount > 0:
                break
              elif amount <= 0:
                   print("enter the number greater  than 0")
         else:
            print("please !! enter a number")     

    return amount           
def get_lines(): # function to get number of lines to bet on
    while True:
         lines=input("enter the lines to bet on (1-" + str(MAX_LINES)  + ")?:") #concatenation method to change int into str and concat
         if lines.isdigit():
              lines=int(lines)
              if 1 <= lines <= MAX_LINES: # to check if the entered lines is within the limit
                break
              else:
                   print("please !! enter a valid number  lines")
         else:
            print("please !! enter a number")  

    return lines

def get_bet(): # function to get bet amount
    while True:
         amount=input("what would you like to bet on each line: $")
         if amount.isdigit():
              amount=int(amount)
              if MIN_BET <= amount <= MAX_BET:
                break
              else:
                  print(f" the bet must be between ${MIN_BET} and ${MAX_BET}")
         else:
            print("please !! enter a number")    
    return amount         


def main():
    balance=deposit()  #get the deposit amount    
    lines=get_lines()  # get the number of lines to bet on
    while True:
        bet=get_bet() # get the bet amount
        total_bet=bet * lines # calculate the total bet
        if total_bet > balance:
            print("you don't have enough balance to bet !!")
        else :
            break
    print(f"you are betting ${bet} on {lines} lines, total bet is ${total_bet}")
    
    
main()