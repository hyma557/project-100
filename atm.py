
class Atm :
    def __init__(self , cardnumber, pin):
        self.cardnumber = cardnumber
        self.pinb = pin

    def balanceinquiry(self):
        print("Your balance is: 10000Rs")

    def cashwithdrawal(self, amount):
        new_amount = 10000-amount
        ptint("You withdraed: " + str(amount) + "Your remaining balance is :" + str(new_amount))

def main():
    name = inpute("hello what is your name?")
    print("Hello" + name)
    cardnumber = input("Inser your card number: ")
    pin = input("Enter your pin: ")
    new_user = atm(cardnumber, pin)

    print("choose your activity")
    print("1 balance Inquiry")
    print("2 Cash withdrawal")
    activity = int(input("Enter the activity: "))
    
    if(activity == 1):
        new_user.balanceinquiry()
    elif(activity == 2):
        amount = int(input("Enter the amount"))
        new_user.cashwithdrawal(amount)
    else:
        print("Enter valid pin")

main()            
    