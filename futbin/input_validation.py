# ---- Tests if command line arguments provided by user are valid
possibleVersions = ["all_versions", "icons", "Gold", "Gold_IF", "All_Specials"]
possiblePositions = ["all_positions", "Attackers", "Midfielders", "Defenders"]
possibleNations = ["all_nations", "Brazil", "Spain", "England", "France", "Germany", "Italy", "Portugal", "Argentina"]
possibleLeagues = ["all_leagues", "Premier_League", "LaLiga_Santander", "Serie_A_TIM", "Bundesliga", "Ligue_1_Conforama"]

def validateInputs(version, position, nation, league, minPace, minPrice, maxPrice):
    selectorsAreValid = True

    if version not in possibleVersions:
        print("You have made a typo, " + version + " is not a valid selector.")
        print()
        selectorsAreValid = False

    if position not in possiblePositions:
        print("You have made a typo, " + position + " is not a valid selector.")
        print()
        selectorsAreValid = False

    if nation not in possibleNations:
        print("You have made a typo, " + nation + " is not a valid selector.")
        print()
        selectorsAreValid = False

    if league not in possibleLeagues:
        print("You have made a typo, " + league + " is not a valid selector.")
        print()
        selectorsAreValid = False

    if int(minPace) < 1 or int(minPace) > 99:
        print("You have made a typo, the minimum pace has to be a value between 1 and 99. You typed: " + str(minPace))
        print()
        selectorsAreValid = False

    if int(minPrice) < 0 or int(minPrice) > 15000000:
        print("You have made a typo, the minimum price has to be a value between 0 and 15 million. You typed: " + str(minPrice))
        print()
        selectorsAreValid = False

    if int(maxPrice) < 0 or int(maxPrice) > 15000000:
        print("You have made a typo, the maximum price has to be a value between 0 and 15 million. You typed: " + str(maxPrice))
        print()
        selectorsAreValid = False

    if not selectorsAreValid:
        print("At least one of the selectors you have used is incorrect - please see above and try again!")

    return selectorsAreValid
