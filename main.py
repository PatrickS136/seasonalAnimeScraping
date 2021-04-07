from bs4 import BeautifulSoup
import requests

# Displaying the prompts
print("\nThis program will scrape myanimelist for anime titles of a minimum rating\n")
num=input("\nEnter the minimum rating as a single digit decimal number: ")

# Scraping the website
data=requests.get("https://myanimelist.net/anime/season").text

soup=BeautifulSoup(data,"html.parser")

# Titles
titleTags=soup.select(selector="#content > div.js-categories-seasonal > div:nth-child(1) > .js-seasonal-anime .link-title")
titles=[i.getText() for i in titleTags]

# Ratings
ratingTags=titleTags=soup.select(selector="#content > div.js-categories-seasonal > div:nth-child(1) > .js-seasonal-anime .score")
ratings=[j.getText()[9:13] for j in ratingTags]

# Results 
print(f"\n\nHere are the new animes with at least {num} ratings: \n\n")

for i in range(len(ratings)):
    if (ratings[i][0]>=num[0] and ratings[i][2]>=num[2]) and ratings[i][0]<="9":
        print(f"({ratings[i]}) {titles[i]}")

print("\nThank you for using the program\n")