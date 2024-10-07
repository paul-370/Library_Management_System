#import libraries
from pwinput import pwinput
from user_management import *
from database_creation import *



##Starting of the library control##

def start():
    wrong_option = 5
    failed_auth = 5

    while True:
        print('------------------------------------------')
        print('|                  Home                  |')
        print('------------------------------------------')
        print('|          1. user Login              |')
        print('|          2. user Register           |')
        print('|          3. Librarian Login            |')
        print('|          4. Librarian Register         |')
        print('------------------------------------------')
        print('Press enter to exit')
        print('Enter your option')
        choice = input('---> ').strip()

        if len(choice) == 0 or wrong_option == 0:
            break

        match choice:
            case '1':
                if failed_auth < 0:
                    break
                print('Enter your ID ')
                usr_id = input('---> ')

                print('Enter your Password')
                usr_pass = pwinput('---> ', mask='x')

                if len(usr_id) == 0 or len(usr_pass) == 0:
                    print('------------------------------------------')
                    print('|         Error : Invalid Entry!         |')
                    print(f'|      Remaining attempts : {failed_auth}      |')
                    print('------------------------------------------')
                    failed_auth -= 1
                    continue

                usr_valid = user_authenticate(usr_id, usr_pass)

                if usr_valid:
                    print('------------------------------------------')
                    print('|                 Hello!                 |')
                    print('------------------------------------------')
                    #print(usr_obj)
                    print('------------------------------------------')
                    #Menu function
                    usr_options()
                    
                else:
                    print('------------------------------------------')
                    print('|    Error : Authentication Failed!      |')
                    print(f'|    Remaining attempts : {failed_auth}              |')
                    print('------------------------------------------')
                    failed_auth -= 1

            case '2':
                status = False
                while True:
                    print('Enter your Name')
                    usr_name = input('---> ').strip()

                    print('Enter your Password')
                    usr_pass_1 = pwinput('---> ', mask='x').strip()

                    print('Re-enter your Password')
                    usr_pass_2 = pwinput('---> ', mask='x').strip()


                    print('Email')
                    usr_email = input('---> ')

                    print('Role')
                    usr_role = input('---> ')

                    if usr_pass_1 != usr_pass_2:
                        print('------------------------------------------')
                        print('|          Password not matching         |')
                        print('|          Press 1 for Re-attempt         |')
                        print('|           Press enter to exit          |')
                        print('------------------------------------------')
                        ch = input('---> ')
                        if ch == '1':
                            continue
                        else:
                            break

                    if len(usr_name) < 1 or len(usr_pass_1) < 1 or len(usr_email) < 1 or len(usr_role) < 1:
                        print('------------------------------------------')
                        print('|          Please enter a valid User details         |')
                        print('|          Press 1 for Re-attempt         |')
                        print('|           Press enter to exit          |')
                        print('------------------------------------------')
                        ch = input('---> ')
                        if ch == '1':
                            continue
                        else:
                            break
                        
                    else:
                        status = True
                        break

                if status:
                    add_user(name=usr_name, password=usr_pass_1, email=usr_email, role=usr_role)

            case '3':
                if failed_auth < 0:
                    break
                print('Enter your ID')
                lib_id = input('---> ').strip()

                print('Enter your Password')
                lib_pass = pwinput('---> ', mask='x').strip()

                if len(lib_id) == 0 or len(lib_pass) == 0:
                    print('------------------------------------------')
                    print('|         Error : Invalid Entry!         |')
                    print(f'|      Remaining attempts : {failed_auth}      |')
                    print('------------------------------------------')
                    failed_auth -= 1
                    continue

                lib_valid = librarian_authenticate(lib_id, lib_pass)

                if lib_valid:
                    print('------------------------------------------')
                    print('|                 Hello!                 |')
                    print('------------------------------------------')
                    # print(lib_obj)
                    print('------------------------------------------')

                    lib_options()
                else:
                    print('------------------------------------------')
                    print('|    Error : Authentication Failed!      |')
                    print(f'|    Remaining attempts : {failed_auth}              |')
                    print('------------------------------------------')
                    failed_auth -= 1
            
            case '4':
                status = False
                while True:
                    print('Enter your Name')
                    lib_name = input('---> ').strip()

                    print('Enter your Password')
                    lib_pass_1 = pwinput('---> ', mask='x').strip()

                    print('Re-enter your Password')
                    lib_pass_2 = pwinput('---> ', mask='x').strip()

                    print('Enter your Email')
                    lib_email = input('---> ').strip()

                    print('Enter your Role')
                    lib_role = input('---> ').strip()

                    if lib_pass_1 != lib_pass_2:
                        print('------------------------------------------')
                        print('|          Password not matching         |')
                        print('|          Press 1 for Re-attempt         |')
                        print('|           Press enter to exit          |')
                        print('------------------------------------------')
                        ch = input('---> ')
                        if ch == '1':
                            continue
                        else:
                            break
                    
                    if len(lib_name) < 1 or len(lib_pass_1) < 1 or len(lib_email) < 1 or len(lib_role) < 1:
                        print('------------------------------------------')
                        print('|          Please enter a valid User details         |')
                        print('|          Press 1 for Re-attempt         |')
                        print('|           Press enter to exit          |')
                        print('------------------------------------------')
                        ch = input('---> ')
                        if ch == '1':
                            continue
                        else:
                            break
                        
                    else:
                        status = True
                        break

                if status:
                    add_librarian(name=lib_name, password=lib_pass_1, email=lib_email, role=lib_role)
            
            case _:
                print('------------------------------------------')
                print('|       Enter the mentioned choices      |')
                print(f'|       Remaining attempts : {wrong_option}           |')
                print('------------------------------------------')
                wrong_option -= 1


##End of library control##

if __name__ == '__main__':
    create_tables()
    start()