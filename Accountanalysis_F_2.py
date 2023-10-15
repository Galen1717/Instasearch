def Function_2():
    print("Welcome to account analysis. Please select an option:")
    print("REMINDER!")
    print("PLEASE INPUT THE RIGHT USERNAME IN EVERY SECTION!WRITTING WRONG USERNAME CAN RESULT")
    print("ERRORS IN SEARCHING FOR ACCOUNT, PLEASE MAKE SURE THAT THE USERNAME YOU ENTERED")
    print("HAS BEEN VERIFIED AND MATCHES THE ACCOUNT YOU WANT TO SEARCH FOR!")
    print("=======================================================================")
    print("1. User Details")
    print("2. Download Profile Picture")
    print("3. Email Extraction")
    print("0.Exit")
    while True:
        choice = input("Choice: ")

        if choice == '1':
            print("WELCOME TO USER DETAILS")
            print("This section will display Username,User ID,Number of Posts, Followers,Following,Bio,And External URL")
            print("REMINDER!")
            print("Please input the right username")
            print("=======================================================================")
                  
            bot = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(bot.context, username=input("Username: "))
            print("Username:", profile.username)
            print("User ID:", profile.userid)
            print("Number of Posts:", profile.mediacount)
            print("Followers Count:", profile.followers)
            print("Following Count:", profile.followees)
            print("Bio:", profile.biography)
            print("External URL:", profile.external_url)
            print("=======================================================================")
            Function_2()
        elif choice == '2':
            print("REMINDER!!")
            print("THE PHOTO WILL BE DOWNLOADED IN THIS PATH (FOR THIS CURRENT VERSION), C:\\Users\\Windows\\AppData\\Local\\Programs\\Python\\Python311")
            print("WARNING!!")
            print("USERS CANT DOWNLOAD INSTAGRAM PHOTO PROFILE REPEATEDLY FROM THE SAME USER")
            print("=======================================================================")
            ig = instaloader.Instaloader()
            dp = input("Enter Insta username: ")
            ig.download_profile(dp, profile_pic_only=True)
            print("=======================================================================")
            print("Please check the donwloaded photo on this path: C:\\Users\\Windows\\AppData\\Local\\Programs\\Python\\Python311")
            Function_2()
        elif choice == '3':
            print("Welcome to Email Extraction!")
            print("This section will extract the email of user if the user attach their email on their bio")
            print("=======================================================================")
            bot = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(bot.context, username=input("Username: "))
            emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
            if emails:
                print("Emails extracted from bio:")
                print(emails)
            else:
                print("No email attached")
                print("=======================================================================")
            Function_2()
        elif choice == '0':
            break
        else:
            print("Invalid choice")
    Menu()
