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
c = 1
box3 = []

box1 = data_file["prime_genre"].tolist()
box2 = data_file["user_rating"].tolist()
box2 = [str(i) for i in box2]
for x in box1:
    for y in box2[c::]:
        c += 1
        box3.append(x+y)
        break
    
for i in box3:
    if "Games" in str(i) and "2.5" in str(i):
        game += 1
    elif "Entertainment" in str(i) and "2.5" in str(i):
        entertainment += 1
    elif "Education" in str(i) and "2.5" in str(i):
        education += 1
    elif "Photo & Video" in str(i) and "2.5" in str(i):
        photo += 1
    elif "Utilities" in str(i) and "2.5" in str(i):
        utilities += 1
    elif "Health & Fitness" in str(i) and "2.5" in str(i):
        health += 1
    elif "Productivity" in str(i) and "2.5" in str(i):
        productivity += 1
    elif "Social Networking" in str(i) and "2.5" in str(i):
        social += 1
    elif "Lifestyle" in str(i) and "2.5" in str(i):
        life += 1
    elif "Music" in str(i) and "2.5" in str(i):
        music += 1
    elif "Shoping" in str(i) and "2.5" in str(i):
        shop += 1
    elif "Sports" in str(i) and "2.5" in str(i):
        sports += 1
    elif "Book" in str(i) and "2.5" in str(i):
        book += 1
    elif "Finance" in str(i) and "2.5" in str(i):
        finance += 1
    elif "Travel" in str(i) and "2.5" in str(i):
        travel += 1
    elif "News" in str(i) and "2.5" in str(i):
        news += 1
    elif "Weather" in str(i) and "2.5" in str(i):
        weather += 1
    elif "Reference" in str(i) and "2.5" in str(i):
        reference += 1
    elif "Food & Drink" in str(i) and "2.5" in str(i):
        food += 1
    elif "Business" in str(i) and "2.5" in str(i):
        business += 1
    elif "Navigation" in str(i) and "2.5" in str(i):
        navigation += 1
    elif "Medical" in str(i) and "2.5" in str(i):
        medical += 1
    elif "Catalogs" in str(i) and "2.5" in str(i):
        catalogs += 1


print("RATE 2.5")
      
print("Games :", game)
print("Entertainment :", entertainment)
print("Education :", education)
print("Photo & Video :", photo)
print("Utilities :", utilities)
print("Health & Fitness :", health)
print("Productivity :", productivity)
print("Social Networking :", social)
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


    







    
