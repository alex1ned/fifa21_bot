# --------------------------------- IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from sys import exit


# --------------------------------- GLOBAL VARIABLES
# ----- Path where the chromedriver.exe is saved
PATH = "/usr/local/bin/chromedriver"

# ----- Webpages
FUTBIN_PLAYERS = "https://www.futbin.com/players"
FUTBIN_BASE = "https://www.futbin.com"

# ----- Variables given by command line !!! need updates
playerVersion = "Gold"
playerPosition = "Attackers"
playerNation = "all_nations"
playerLeague = "LaLiga_Santander"
minPace = int("70")
minPrice = int("10000")
maxPrice = int("90000")

# ---- Tests if command line arguments are valid
possibleVersions = ["all_versions", "icons", "Gold", "Gold_IF", "All_Specials"]
possiblePositions = ["all_positions", "Attackers", "Midfielders", "Defenders"]
possibleNations = ["all_nations", "Brazil", "Spain", "England", "France", "Germany", "Italy", "Portugal", "Argentina"]
possibleLeagues = ["all_leagues", "Premier_League", "LaLiga_Santander", "Serie_A_TIM", "Bundesliga", "Ligue_1_Conforama"]

selectorsAreValid = True

if playerVersion not in possibleVersions:
    print("You have made a typo, " + playerVersion + " is not a valid selector.")
    print()
    selectorsAreValid = False

if playerPosition not in possiblePositions:
    print("You have made a typo, " + playerPosition + " is not a valid selector.")
    print()
    selectorsAreValid = False

if playerNation not in possibleNations:
    print("You have made a typo, " + playerNation + " is not a valid selector.")
    print()
    selectorsAreValid = False

if playerLeague not in possibleLeagues:
    print("You have made a typo, " + playerLeague + " is not a valid selector.")
    print()
    selectorsAreValid = False

if minPace < 1 or minPace > 99:
    print("You have made a typo, the minimum pace has to be a value between 1 and 99. You typed: " + str(minPace))
    print()
    selectorsAreValid = False

if minPrice < 0 or minPrice > 15000000:
    print("You have made a typo, the minimum price has to be a value between 0 and 15 million. You typed: " + str(minPrice))
    print()
    selectorsAreValid = False

if maxPrice < 0 or maxPrice > 15000000:
    print("You have made a typo, the maximum price has to be a value between 0 and 15 million. You typed: " + str(maxPrice))
    print()
    selectorsAreValid = False

if not selectorsAreValid:
    print("At least one of the selectors you have used is incorrect - please see above and try again!")
    exit()



# --------------------------------- MAIN PROGRAM
# --- XPATHS and css selectors
allowCookiesXpath = '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'
sortByPriceXpath = '//*[@id="repTb"]/thead/tr/th[5]/a'
playerTableSelector = '#repTb tbody'

# --- Open Futbin
driver = webdriver.Chrome(PATH)
driver.get(FUTBIN_PLAYERS)

# --- Wait until webpage has loaded and allow cookies
allowCookies = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, allowCookiesXpath))
)
allowCookies.click()

# --- Maximise screen window
driver.maximize_window()


# --- Version selector
# Case for all versions
if playerVersion == "all_versions":
    print("All versions are selected")

# Else if you select a specific version
else:
    # --- Hover over versions
    versionsLink = driver.find_element_by_link_text("Version")
    hover = ActionChains(driver).move_to_element(versionsLink)
    hover.perform()

    if playerVersion == "icons" or playerVersion == "Gold":
        # --- Hover over the version
        versionLink = driver.find_element_by_link_text(playerVersion)
        hover = ActionChains(driver).move_to_element(versionLink)
        hover.perform()

        # Select all icons
        if playerVersion == "icons":
            # --- Click on "All" under icons
            print("All icons are selected.")
            versionLink = driver.find_element_by_link_text("All")
            versionLink.click()

        # Select all gold
        elif playerVersion == "Gold":
            # --- Click on "All Gold" under Gold
            print("All gold players are selected.")
            versionLink = driver.find_element_by_link_text("All Gold")
            versionLink.click()

    # !!! All_Specials does not work yey, GOLD_IF works fine
    elif playerVersion == "Gold_IF" or playerVersion == "All_Specials":
        playerVersionText = playerVersion.replace('_', ' ')
        print("All " + playerVersionText + " players are selected.")
        versionLink = driver.find_element_by_link_text(playerVersionText)
        versionLink.click()


# --- Position selector
# Case for all positions
if playerVersion == "all_versions":
    print("All positions are selected")

else:
    print("All " + playerPosition + " are selected.")
    # --- Hover over positions
    positionsLink = driver.find_element_by_link_text("Positions")
    hover = ActionChains(driver).move_to_element(positionsLink)
    hover.perform()
    # --- click on position
    positionLink = driver.find_element_by_link_text(playerPosition)
    positionLink.click()


# --- Nation selector
if playerNation == "all_nations":
    print("All nations are selected")

else:
    print("All players from " + playerNation + " are selected.")
    # --- Hover over 'Nations'
    nationsLink = driver.find_element_by_link_text("Nations")
    hover = ActionChains(driver).move_to_element(nationsLink)
    hover.perform()

    # --- Click on input field and type the nation
    nationsInput = driver.find_element_by_css_selector("#Nation")
    nationsInput.send_keys(playerNation)

    # --- Click on the search result
    nationSearchResult = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, playerNation))
    )
    nationSearchResult.click()


# --- League selector
if playerLeague == "all_leagues":
    print("All leagues are selected")

else:
    playerLeagueText = playerLeague.replace('_', ' ')
    firstWordOfLeage = playerLeagueText.split(' ')[0]
    print("All players from " + playerLeagueText + " are selected.")
    # --- Hover over 'League'
    leaguesLink = driver.find_element_by_link_text("Leagues")
    hover = ActionChains(driver).move_to_element(leaguesLink)
    hover.perform()

    # --- Click on input field and type the league
    leaguesInput = driver.find_element_by_css_selector("#League")
    leaguesInput.send_keys(firstWordOfLeage)

    sleep(0.5)
    # --- Click on the search result
    leagueSearchResult = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, playerLeagueText))
    )
    leagueSearchResult.click()



# --- Pace selector
# Hover over 'Stats'
statsLink = driver.find_element_by_link_text("Stats")
hover = ActionChains(driver).move_to_element(statsLink)
hover.perform()

# Type in the min and max pace
minPaceInput = driver.find_element_by_xpath("/html/body/div[8]/div/div[4]/div[2]/ul/div/ul/li[10]/ul/li/div/div[1]/div[2]/div/span[2]/input[1]")
maxPaceInput = driver.find_element_by_xpath("/html/body/div[8]/div/div[4]/div[2]/ul/div/ul/li[10]/ul/li/div/div[1]/div[2]/div/span[2]/input[2]")
minPaceInput.send_keys(str(minPace))
maxPaceInput.send_keys("99")

# Click on the filter button
filterButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "filter_stats"))
)
filterButton.click()



# --- Price selector
# Hover over 'PS' (the price selector)
priceLink = driver.find_element_by_link_text("PS")
hover = ActionChains(driver).move_to_element(priceLink)
hover.perform()

# Type in the min and max price
minPriceInput = driver.find_element_by_id("MinPS_Price")
maxPriceInput = driver.find_element_by_id("MaxPS_Price")
minPriceInput.send_keys(str(minPrice))
maxPriceInput.send_keys(str(maxPrice))

# Click on the filter button
filterButton = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div[4]/div[2]/ul/div/ul/li[11]/ul/li[3]/button"))
)
filterButton.click()






sleep(0.5)



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
    playerTable = driver.find_element_by_css_selector(playerTableSelector)
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
    price = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "ps-lowest-1"))
    )
    cardName = driver.find_element_by_class_name("pcdisplay-name").text
    value.append(price.text)
    value.append(cardName)
    sleep(1)
    i += 1
    if i == 2:
        break

# Print out first 5 items to see how it is formatted
i = 0
for key, value in playerDatabase.items():
    value[-2] = int(value[-2].replace(',', ''))
    value[-2] = float(value[-2])
    print(value)
    i += 1
    if i == 2:
        break












# ------------------- END OF FILE ------------------------------------------
