import numpy as np
import pandas as pd
import json

game = 0
entertainment = 0
education = 0
photo = 0
utilities = 0
health = 0
productivity = 0
social = 0
life = 0
music = 0
shop = 0
sports = 0
book = 0
finance = 0
travel = 0
news = 0
weather = 0
reference = 0
food = 0
business = 0
navigation = 0
medical = 0
catalogs = 0

data_file = pd.read_csv('AppleStore.csv')
gen = data_file[["prime_genre","user_rating"]]

for i in gen.iterrows():
    if "Games" in str(i) and " 0" in str(i):
        game += 0
    elif "Entertainment" in str(i) and " 0" in str(i):
        entertainment += 0
    elif "Education" in str(i) and " 0" in str(i):
        education += 0
    elif "Photo & Video" in str(i) and " 0" in str(i):
        photo += 0
    elif "Utilities" in str(i) and " 0" in str(i):
        utilities += 0
    elif "Health & Fitness" in str(i) and " 0" in str(i):
        health += 0
    elif "Productivity" in str(i) and " 0" in str(i):
        productivity += 0
    elif "Social Networking" in str(i) and " 0" in str(i):
        social += 0
    elif "Lifestyle" in str(i) and " 0" in str(i):
        life += 0
    elif "Music" in str(i) and " 0" in str(i):
        music += 0
    elif "Shoping" in str(i) and " 0" in str(i):
        shop += 0
    elif "Sports" in str(i) and " 0" in str(i):
        sports += 0
    elif "Book" in str(i) and " 0" in str(i):
        book += 0
    elif "Finance" in str(i) and " 0" in str(i):
        finance += 0
    elif "Travel" in str(i) and " 0" in str(i):
        travel += 0
    elif "News" in str(i) and " 0" in str(i):
        news += 0
    elif "Weather" in str(i) and " 0" in str(i):
        weather += 0
    elif "Reference" in str(i) and " 0" in str(i):
        reference += 0
    elif "Food & Drink" in str(i) and " 0" in str(i):
        food += 0
    elif "Business" in str(i) and " 0" in str(i):
        business += 0
    elif "Navigation" in str(i) and " 0" in str(i):
        navigation += 0
    elif "Medical" in str(i) and " 0" in str(i):
        medical += 0
    elif "Catalogs" in str(i) and " 0" in str(i):
        catalogs += 0


print("RATE
      
print("Games :", game)
print("Entertainment :", entertainment)
print("Education :", education)
print("Photo & Video :", photo)
print("Utilities :", utilities)
print("Health & Fitness :", health)
print("Productivity & Fitness :", productivity)
print("Social Networking :", soci
      al)
print("Lifestyle :", life)
print("Music :", music)
print("Shoping :", shop)
print("Sports :", sports)
print("Book :", book)
print("Finance :", finance)
print("Travel :", travel)
print("News :", news)
print("Weather :", weather)
print("Reference :", reference)
print("Food & Drink :", food)
print("Business :", business)
print("Navigation :", navigation)
print("HMedical :", medical)
print("Catalogs :", catalogs)

print("Max :", max(game, entertainment, education, photo, utilities, health\
          , productivity, social, life, music, shop, sports\
          , book, finance, travel, travel, news, weather, reference\
          , food, business, navigation, medical, catalogs))

