def Function_3():
    print("Welcome to Hastags and Mentions Extraction")
    print("This section will extracted:")
    print("1.Number of post")
    print("2.Post URL")
    print("3.Caption")
    print("4.Hastags Extraction")
    print("5.Mention Extraction")
    print("=======================================================================")
    def extract_hashtags_and_mentions(caption):
        hashtags = re.findall(r'#(\w+)', caption)
        mentions = re.findall(r'@(\w+)', caption)
        return hashtags, mentions

    loader = instaloader.Instaloader()

    def print_post_with_details(username):
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
            post_counter = 0
            for post in profile.get_posts():
                post_counter += 1
                print(f"Post #{post_counter}")
                print("Post URL:", f"https://www.instagram.com/p/{post.shortcode}")
                print("Caption:", post.caption)
                hashtags, mentions = extract_hashtags_and_mentions(post.caption)
                print("Hashtags:", hashtags)
                print("Mentions:", mentions)
                print("-----------------------------------------")
        except instaloader.exceptions.ProfileNotExistsException:
            print("Instagram account does not exist.")
        except instaloader.exceptions.ProfilePrivateException:
            print("The account is private, cannot check on private accounts.")
            return

    username = input("Enter Instagram username: ")
    print_post_with_details(username)

    print("What do you want?")
    print("1.Extract another username?")
    print("2.Go back to menu")

    choice = input("Choice: ")
    if choice == '1':
        Function_3()
    elif choice == '2':
        Menu()
    else:
        print("WRONG CHOICE!")
    Menu()
