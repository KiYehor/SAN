import random
x=True
y=False
while x==True:
    choose=int(input("1. register\n2. login"));
    class User:
        def  __init__(self, login):
            self.login =login
            self.password =password
    if choose==1:
            print('Enter login:')
            login=input()
            print('enter password:')
            password=input()
            new_user=User(login)
            new_user.password
    if choose==2:
        print('enter login:')
        login_check=input()
        print('enter password:')
        password_check=input()
        if login_check!= login:
            print("not correct login");
        else:
            if password_check!= password:
                print("not correct password");
            else:
                y=True
            while y==True:
                menu_choose=int(input("1. history\n2. account balance\n3. possibility of payment\n4.payments\n5.Exit"));
                account_balance=random.randint(1,1000)
                historia=random.randint(1, 1000);
                match menu_choose:
                    case 1:
                        test_list = ['from your account', 'to your account'];
                        rand_idx = random.randrange(len(test_list));
                        random_text = test_list[rand_idx];
                        print(historia, 'pln', random_text);
                    case 2:
                        a=account_balance+historia
                        print(a, 'pln')
                    case 3:
                        w3=int(input("1.Pay\n2. back"))
                        if w3==1:
                            pay=int(input("enter the payment amount"))
                            if pay<a:
                                a=a-pay
                            else:
                                print('Insufficient funds')
                        print(" ")
                    case 4:
                        Names =['John', 'Tailor', 'Igor', 'Anna', 'Anna', 'Alexander','Igor']
                        set=(Names)
                        rand_n = random.randrange(len(Names))
                        random_names = set[rand_n]
                        pay1=random.randint(1,1000)
                        thisdict = dict(name = random_names, payment = pay1, country = "Norway")
                        print(thisdict)
                    case 5:
                        break
