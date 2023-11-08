class ATM:

    def __init__(self):     
        self.balance=0    # initially_bank_balance
        print("Hello, This is a withdrawl and deposite machine")
            
    def deposite(self): 
        amount = float(input("Enter amount to be deposited : "))  # amount):
        self.balance=self.balance+amount   # balance= balance+amount
        print("depo amt",amount)
        
    def update_mobile_number(self,new_mobile_number):
        self.new_mobile_number = new_mobile_number
        print("Mobile Number is", self.new_mobile_number)
        
    def withdrawl(self):
        amount = float(input("Enter amount to be withdrawl: "))  
        if self.balance>=amount:
            self.balance=self.balance-amount  
            print("you withdraw:",amount)
            
        else:
            print("low balance ")    
            
    def Check_Balance(self):
        print("\n Net available balance",self.balance)
        
    def Change_Pin(self,new_pin):
        self.new_pin=new_pin
        print("Pin is",self.new_pin)
        
                       
s=ATM()  #object created
                       
s.deposite()  #call deposit function

a = input("Do you want to change the mobile number: ")
if a == 'yes':
    new_mobile_no = int(input("Enter Your mobile number: "))
    print("mobile_number updated successfully")



s.update_mobile_number(new_mobile_no)
s.withdrawl() 

p = input("Do you want to change your pin: ")
if p == 'yes':
    newpin = int(input("Enter your New Pin: "))
    print("pin updated successfully")

s.Change_Pin(newpin)


s.Check_Balance()