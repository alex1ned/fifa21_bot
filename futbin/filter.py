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




def filterVersions(driver, playerVersion):
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


def filterPositions(driver, playerPosition):
    # Case for all positions
    if playerPosition == "all_positions":
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


def filterNation(driver, playerNation):
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


def filterLeague(driver, playerLeague):
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


def filterPace(driver, minPace):
    # Hover over 'Stats'
    print("All players with pace from " + minPace + " to 99 are selected.")
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


def filterPrice(driver, minPrice, maxPrice):
    # Hover over 'PS' (the price selector)
    print("All players with a price from " + minPrice + " to " + maxPrice + " are selected.")
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


def filterPlayers(driver, playerVersion, playerPosition, playerNation, playerLeague, minPace, minPrice, maxPrice):
    filterVersions(driver, playerVersion)
    filterPositions(driver, playerPosition)
    filterNation(driver, playerNation)
    filterLeague(driver, playerLeague)
    filterPace(driver, minPace)
    filterPrice(driver, minPrice, maxPrice)
