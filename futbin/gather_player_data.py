# --------------------------------- IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from sys import exit
import sys

from input_validation import validateInputs
from filter import filterPlayers

# --------------------------------- GLOBAL VARIABLES
# ----- Path where the chromedriver.exe is saved
PATH = "/usr/local/bin/chromedriver"

# ----- Webpages
FUTBIN_PLAYERS = "https://www.futbin.com/players"
FUTBIN_BASE = "https://www.futbin.com"

# ----- Variables given by command line !!! need updates
playerVersion = sys.argv[1]
playerPosition = sys.argv[2]
playerNation = sys.argv[3]
playerLeague = sys.argv[4]
minPace = sys.argv[5]
minPrice = sys.argv[6]
maxPrice = sys.argv[7]

# playerVersion = "Gold"
# playerPosition = "Attackers"
# playerNation = "all_nations"
# playerLeague = "LaLiga_Santander"
# minPace = int("70")
# minPrice = int("10000")
# maxPrice = int("90000")

# ----- Test if command line arguments provided by user are valid
isValid = validateInputs(playerVersion, playerPosition, playerNation, playerLeague, minPace, minPrice, maxPrice)
if not isValid:
    exit()

# --------------------------------- MAIN PROGRAM
# --- Open Futbin
driver = webdriver.Chrome(PATH)
driver.get(FUTBIN_PLAYERS)

# --- Wait until webpage has loaded and allow cookies
allowCookies = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))
)
allowCookies.click()

# --- Maximise screen window
driver.maximize_window()

# --- Version selector
filterPlayers(driver, playerVersion, playerPosition, playerNation, playerLeague, minPace, minPrice, maxPrice)

sleep(0.5)


# --- Scrape data
numberOfPages = 1
try:
    numberOfPagesParent = driver.find_element_by_css_selector("nav ul.pagination")
    numberOfPagesChildren = numberOfPagesParent.find_elements_by_tag_name("li")
    numberOfPages = int(numberOfPagesChildren[-2].text)
except:
    numberOfPages = 1

print()
print("The number of pages is " + str(numberOfPages))
print()

# Get the correct url parts to switch across pages
currentURL = driver.current_url
urlParts = currentURL.split("page=1")
pagesURLstart = urlParts[0] + "page="
pagesURLend = urlParts[-1]



# Dictionary to store all player details apart from price (name, rating, version)
playerDatabase = {}

for i in range(0, numberOfPages):
    playerTable = driver.find_element_by_css_selector('#repTb tbody')
    players = playerTable.find_elements_by_tag_name('tr')

    # Get player details for each page
    for player in players:
        playerLink = player.find_element_by_class_name("player_name_players_table")

        # Variables per player
        name = playerLink.text
        rating = player.find_element_by_css_selector("span.rating").text
        webAddress = FUTBIN_BASE + player.get_attribute("data-url")
        version = player.find_element_by_class_name("mobile-hide-table-col").text

        playerDatabase[name+rating] = [name, rating, version, webAddress]

    # Change page and sleep program for 2 seconds
    driver.get(pagesURLstart + str(i+1) + pagesURLend)
    sleep(0.2)

# Go to every player's webpage and get their price, cardName, league, nation
i = 0
for key, value in playerDatabase.items():
    driver.get(value[-1])
    sleep(1)
    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ps-lowest-1"))
    )
    cardName = driver.find_element_by_class_name("pcdisplay-name").text
    value.append(price.text)
    value.append(cardName)
    sleep(1)
    i += 1
    if i == 4:
        break

# Print out first 5 items to see how it is formatted
i = 0
for key, value in playerDatabase.items():
    value[-2] = int(value[-2].replace(',', ''))
    value[-2] = int(value[-2])
    print(value)
    i += 1
    if i == 4:
        break


# --- Quit browser at the end
driver.quit()

# ------------------- END OF FILE ------------------------------------------
