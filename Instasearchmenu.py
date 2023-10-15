def Menu():
    logo = r"""
                               
.___                 __           _________                           .__      
|   | ____   _______/  |______   /   _____/ ____ _____ _______   ____ |  |__   
|   |/    \ /  ___/\   __\__  \  \_____  \_/ __ \\__  \\_  __ \_/ ___\|  |  \  
|   |   |  \\___ \  |  |  / __ \_/        \  ___/ / __ \|  | \/\  \___|   Y  \ 
|___|___|  /____  > |__| (____  /_______  /\___  >____  /__|    \___  >___|  / 
         \/     \/            \/        \/     \/     \/            \/     \/  1.0


"""
    print(logo)

    
    print("=== Insta Search: Osint Tools for Instagram ===")
    print("Please select your selection!: ")
    print("1. Search Social Media Account")
    print("2. Account Analysis")
    print("3. Hastags and mention extraction")
    print("4. User Guide")
    print("0. Exit")
    print("=======================================================================")
    print("REMINDER!")
    print("if this is your first time using this program,it is highly recommended to read")
    print("the User guide first to get an understanding of how to use this program")
    print("=======================================================================")
    print("WARNING! PLEASE READ!")
    print("PLEASE INPUT THE RIGHT USERNAME IN EVERY SECTION!WRITTING WRONG USERNAME CAN RESULT")
    print("ERRORS IN SEARCHING FOR ACCOUNT, PLEASE MAKE SURE THAT THE USERNAME YOU ENTERED")
    print("HAS BEEN VERIFIED AND MATCHES THE ACCOUNT YOU WANT TO SEARCH FOR!")
    print("=======================================================================")

    while True:
        pilihan = input('Enter your selection: ')

        if pilihan == '1':
            print("WELCOME TO SOCIAL MEDIA SEARCH!")
            print("FOR THIS CURRENT VERSION ONLY CAN SEARCH USERNAME TO:")
            print("1.Instagram")
            print("2.Tiktok")
            print("3.Youtube")
            print("WARNING! PLEASE READ!")
            print("PLEASE INPUT THE RIGHT USERNAME IN EVERY SECTION!WRITTING WRONG USERNAME CAN RESULT")
            print("ERRORS IN SEARCHING FOR ACCOUNT, PLEASE MAKE SURE THAT THE USERNAME YOU ENTERED")
            print("HAS BEEN VERIFIED AND MATCHES THE ACCOUNT YOU WANT TO SEARCH FOR!")
            print("=======================================================================")
            print("PLEASE INPUT THE RIGHT USERNAME!")
            username = input('Input username: ')
            Function_1(username)
        elif pilihan == '2':
            Function_2()
        elif pilihan == '3':
            Function_3()
        elif pilihan == '4':
            Function_4()
        elif pilihan == '0':
            break
        else:
            print('ERROR!NOT VALID SELECTION!')

# Menjalankan program -> program start!
Menu()
