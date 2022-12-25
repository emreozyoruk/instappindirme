import instaloader 

ig = instaloader.Instaloader()
dp = input("Instagram Adresini Giriniz: ")
ig.download_profile(dp , profile_pic_only=True)
