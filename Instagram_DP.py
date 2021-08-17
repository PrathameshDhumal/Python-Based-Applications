##############################################################
#
#Author:Prathamesh Dhumal
#Date:3/8/21
#About:Instagram Display Picture Extractor
#
#############################################################
import instaloader

ig = instaloader.Instaloader()
dp = input("Enter insta username:")

ig.download_profile(dp,profile_pic_only =True)
