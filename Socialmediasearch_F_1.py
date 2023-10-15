def Function_1(username):
    instagram_url = f"https://www.instagram.com/{username}/"
    tiktok_url = ""
    youtube_url = ""

    # Function Search TikTok Part
    tiktok_response = requests.get(f"https://www.tiktok.com/@{username}")
    if tiktok_response.status_code == 200:
        tiktok_url = f"https://www.tiktok.com/@{username}/"

    # Youtube
    youtube_response = requests.get(f"https://www.youtube.com/{username}")
    if youtube_response.status_code == 200:
        youtube_url = f"https://www.youtube.com/@{username}/"


    print("Social Media Accounts Found:")
    print(f"Instagram: {instagram_url}")
    print(f"TikTok: {tiktok_url}")
    print(f"Youtube: {youtube_url}")
    print("=====================================================================================")

    print("What do you want?")
    print("1.Search again?")
    print("2.Go back to menu")
    print("=======================================================================")

    choice = input("Choice: ")
    if choice == '1':
        username = input('Input username: ')
        Function_1(username)
    elif choice == '2':
        Menu()
    else:
        print("WRONG CHOICE!")
