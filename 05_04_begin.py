def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
    else:
        print("Insufficnet funds")
    return current_balance

def add2 (number):
    output = number + 2
    return output

answer = add2(3)
print("The answer is: ", answer)

##balance = withdraw_money(10, 200)

##print("Current Balance: ", balance)



