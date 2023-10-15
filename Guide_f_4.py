def Function_4():
    print("Welcome to User Guide!")
    print("Please Select Which Part Do You Want:")
    print("1.Media social Search")
    print("2.Analysis account")
    print("3.Hastags and Mention Extraction")
    print("0. Back to Menu")

    while True:
        choice = input("Choice: ")
        if choice == '1':
            Media_Social_Search_Guide()
        elif choice == '2':
            Analysis_Account_Guide()
        elif choice == '3':
            Hastags_and_Mentions_Guide()
        elif choice == '0':
            break
        else:
            print("ERROR!INVALID CHOICE")
    Menu()


def Analysis_Account_Guide():
    print("Welcome to user guide for Analysis Account!")
    print(" Analysis Account is feature in the program that allows you to analyze Instagram user accounts.")
    print("This feature provides several options, including getting user details, downloading profile photos, and extracting emails from user bios.")
    print("=======================================================================")
    print("Since this section is divided into 3 part, please select selection that you want to know: ")
    print("1.User info")
    print("2.Photo profile download")
    print("3.Email Extraction")
    print("0.Back to user guide menu")

    while True:
        choice = input("Choice: ")
        if choice == '1':
            print("User info is a feature for displaying Instagram account information from inputted users")
            print("this feature will display the Username, User ID, Number of Posts, Followers Count, Following Count, Bio, and External Url.")
            print("=======================================================================")
            print("Guide:")
            print("1. The program will ask you to enter the username of the Instagram user you want to analyze.")
            print("2. Enter the username correctly and make sure you type it correctly.")
            print("3. After entering the username, the program will start the analysis process and retrieve the user details from the account.")
            print("4. User details that will be displayed include username, user ID, number of posts, number of followers, number of followers, biography, and external URL")
            print("5. You can view this information to learn more about the selected Instagram user's account.")
            Analysis_Account_Guide()
        elif choice == '2':
            print("Photo Profile Download is a feature for downloading the photo profile from instagram account that inputted by the user")
            print("=======================================================================")
            print("Guide:")
            print("1. The program will ask you to enter the username of the Instagram user whose profile photo you want to download.")
            print("2. Enter the username correctly and make sure you type it correctly.")
            print("3. After entering the username, the program will start the process of downloading the profile photo from that account.")
            print("4. The profile photo will be downloaded and stored in the program's working directory.")
            print("5. You can use the profile photo for whatever purpose you want.")
            print("=======================================================================")
            print("REMINDER!!")
            print("THE PHOTO WILL BE DOWNLOADED IN THIS PATH (FOR THIS CURRENT VERSION), C:\\Users\\Windows\\AppData\\Local\\Programs\\Python\\Python311")
            print("WARNING!!")
            print("USERS CANT DOWNLOAD INSTAGRAM PHOTO PROFILE REPEATEDLY FROM THE SAME USER")
            print("=======================================================================")
            
            Analysis_Account_Guide()
        elif choice == '3':
            print("Email Extraction is a feature for extracting emails listed in the Instagram account bio, this feature utilizes the re library to extract these emails")
            print("=======================================================================")
            print("Guide: ")
            print("1. The program will ask you to enter the username of the Instagram user you want to analyze.")
            print("2. Enter the username correctly and make sure you type it correctly.")
            print("3. After entering the username, the program will start the analysis process and extract the email from the user's bio.")
            print("4. If a related email is found in the bio, the program will display it.")
            print("5. If there is no associated e-mail, the program will give a message that there is no e-mail attached.")
            Analysis_Account_Guide()
        elif choice == '0':
            break
        else:
            print("ERROR! INVALID CHOICE!")
    Function_4()


        
        
def Media_Social_Search_Guide():
        print("Welcome to user guide for social media search!")
        print("=======================================================================")
        print("The main purpose of this function is to search for user accounts on social media platforms such as Instagram, TikTok, Facebook and YouTube.")
        print("If a user enters an incorrect or invalid username, this function will not be able to find the account in question and will not generate a valid URL for that account.")
        print("So please make sure you input the right username!")
        print("Guide: ")
        print("=======================================================================")
        print("1. Enter the correct username and make sure you type it correctly. (Note that the program does not currently perform username validation,")
        print("so make sure you enter the correct username for accurate results.)")
        print("2. After you enter your username, the program will start a search on several social media platforms.")
        print("3. If an account is found on a certain social media platform, the program will display the URL of that social media account.")
        print("4. For Example: ")
        print("Username input:mrvn_satrio")
        print("Instagram: https://www.instagram.com/mrvn_satrio")
        print("TikTok: https://www.tiktok.com/@mrvn_satrio")
        print("Facebook: https://www.facebook.com/mrvn_satrio")
        print("YouTube:")
        print("Pay attention to the URL that is displayed as a search result. You can click on the URL to go directly to the associated social media account.")
        print("After viewing the search results, the program will give you the option to perform another search by entering another username or returning to the program's main menu.")
        print("=======================================================================")
        Function_4()
def Hastags_and_Mentions_Guide():
        print("Welcome to Hastags and Mention Extraction!")
        print("=======================================================================")
        print("This section is a feature in the program that allows you to extract hashtags and mentions (@ sign) from captions of specific users' Instagram posts.")
        print("Guide:")
        print("=======================================================================")
        print("1. Enter the Instagram username you want to check in the program.")
        print("2. The program will process your request and retrieve information about posts from Instagram accounts that match the username you entered.")
        print("3. After the process is complete, the program will display posting information from that account, including the post URL and caption.")
        print("4. Pay attention to the caption of each post that is displayed. This function will extract hashtags and mentions from each existing caption.")
        print("5. If there are hashtags in the caption, they will be displayed as a separate list.")
        print("For example: Hashtags: #APU #OSINT #Cyber ")
        print("6. If there are mentions (@ sign) in the caption, they will also be displayed as a separate lis")
        print("For example: Mentions: @apuregional_id, @mrvn_satrio, @synstergates")
        print("7. You can note down or use the extracted hashtags and mentions information according to your needs.")
        print("8. After finishing using this feature, the program will give you the option to repeat the process with another Instagram username or return to the program's main menu.")
        print("9. Make sure to enter the correct Instagram username so that this feature can provide accurate results. Also, note that this feature only works on Instagram post captions, and will not find hashtags or mentions in other parts of the user's account.")
        print("10. Please note, this feature will not work on private accounts, and accounts that post without captions and mentions.")
        Function_4()
