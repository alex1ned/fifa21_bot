# --------------------------------- IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# --------------------------------- GLOBAL VARIABLES
# ----- Path where the chromedriver.exe is saved
PATH = "/usr/local/bin/chromedriver"

# ----- Webpages
FUTBIN_PLAYERS = "https://www.futbin.com/players"
FUTBIN_BASE = "https://www.futbin.com"


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


# --- Hover over versions
versionsLink = driver.find_element_by_link_text("Version")
hover = ActionChains(driver).move_to_element(versionsLink)
hover.perform()

# --- Hover over icons
iconsLink = driver.find_element_by_link_text("icons")
hover = ActionChains(driver).move_to_element(iconsLink)
hover.perform()

# --- Click on "All" under icons
allIconsLink = driver.find_element_by_link_text("All")
allIconsLink.click()

sleep(0.5)

numberOfPagesParent = driver.find_element_by_css_selector("nav ul.pagination")
numberOfPagesChildren = numberOfPagesParent.find_elements_by_tag_name("li")
numberOfPages = int(numberOfPagesChildren[-2].text)

# Get the correct url parts to switch across pages
currentURL = driver.current_url
urlParts = currentURL.split("page=1")
pagesURLstart = urlParts[0] + "page="
pagesURLend = urlParts[-1]




# Dictionary to store all player details apart from price (name, rating, version)
playerDatabase = {}

for i in range(1, numberOfPages):
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
    if i == 5:
        break



# Print out first 5 items to see how it is formatted
i = 0
for key, value in playerDatabase.items():
    value[-2] = int(value[-2].replace(',', ''))
    value[-2] = float(value[-2])
    print(value)
    i += 1
    if i == 5:
        break











# ------------------------------------------- SAMPLES
"""
# driver = webdriver.Chrome(PATH)
# driver.get(FUT21_WEB_APP)


# --- Store HTML element to a variable (assume it is a field)
aVariable = driver.find_element_by_name("")

# --- Type in text in a field
aVariable.send_keys("my username")
# --- Hit Enter
aVariable.send_keys(Keys.RETURN)



# --- Get a PARENT by ID and wait 10 sec for page to Download
# --------- and get all children in the parent
try:
    aParent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "theIdOfParent"))
    )

    # --- print out all the text inside the parent (incl children text)
    print(aParent.text)

    # --- get all children and print out their headers
    allChildren = aParent.find_elements_by_tag_name("theTag")
    for child in allChildren:
        header = child.find_element_by_class_name("theClassName")
        print(header.text)
finally:
    driver.quit()

# --- Click on an element
anElement.click()
# --- Go back or forward by a page
dirver.back()
driver.forward()
# --- Clear text of input field before typing in new text
anInputField.clear()


# --- Action chains (see documentation)
# --------- create instance
action = ActionChains(driver)
# click mouse wherever it is
actions.click()
actions.perform()

# --- Implicit wait 5 seconds
diver.implicitly_wait(5)

"""
