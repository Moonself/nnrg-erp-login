from erp import    erplogin
new_session = erplogin()
print("Options  are \n1.login\n2.Get attendance\n3.Get marks\n4.Get both marks and attendance\n5.Exit")
choice = None
while (choice != 8):
    choice  = input('Enter your choice: ')
    match choice:
        case '1':
            new_session.login(input('Enter Roll No. :'))
        case '2':
            new_session.get_atd()
        case '3':
            new_session.get_marks(True,True)
        case '4':
            new_session.get_atd()
            new_session.get_marks(False,False)
        case '5':
            choice = 8

