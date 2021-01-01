<!-- TABLE OF CONTENTS -->
# Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [How to use](#how-to-use)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)


<!-- ABOUT THE PROJECT -->
# About The Project

This project attempts to trade on the web app of FIFA21 to increase the user's coins. The program is a two-fold command line operated application.

1. First the user screens the webpage Futbin for players to gather their stats - most importantly their most recent price. The user can filter which players he wishes to collect data for.
2. Once the above is finished, the user can execute the second programm to trade on the FUT21 web application (part 2 is not finished and wip).

The applications were built on the macintosh OS and have not been tested on any other operating system. The applications use selenium for python to access the webpages and requires the user to have python 3 installed.

<!-- ![AnImage](./readme_images/webpage.png) -->


## Built With
This project has been built using the following frameworks.

###Frameworks / Plugins / Dependencies

* [Python 3](https://www.python.org/download/releases/3.0/)
* [Selenium for python](https://selenium-python.readthedocs.io)
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

###Websites used

* [Futbin](https://www.futbin.com)
* [FUT21 web app](https://www.ea.com/de-de/fifa/ultimate-team/web-app/)



<!-- GETTING STARTED -->
# Getting Started

To get a local copy up and running follow these simple steps.

## Prerequisites

The application requires you to have the following installed:
* Python 3
* Pip or pip3
* Chrome

## Installation

1. Clone the repo
```
git clone https://github.com/alex1ned/travel_planner.git
```
2. Download ChromeDriver and move executable file

* Ensure you have Chrome installed and up to date.
* Download the correct version of ChromeDriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
  * Note that if your standard Chrome is version 87, then your ChromeDriver also needs to be version 87
  * Download the zip file corresponding to your OS
* Unzip the file and move the ChromeDriver executable to the following location using your terminal
  * `/usr/local/bin/chromedriver`

3. Install selenium for python 3

Open your terminal and install selenium using pip3.

```
pip3 install selenium
```

[Here](https://www.youtube.com/watch?v=Xjv1sY630Uc&list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ&index=1) is a tutorial on how to install selenium should you run into difficulties.

Alternatively the you can find the documentation of selenium [here](https://selenium-python.readthedocs.io).


## How to use

The below explains how to use the two applications once you have successfully completed the installation above.

**Retrieve player stats from futbin**

With your terminal navigate to this project's folder and move into the folder **futbin**. The application is excuted using `python3 gather_player_data.py` followed by a chain of selectors. The possible values of selectors are explained below.

```
python3 gather_player_data.py [version] [position] [nation] [league] [min pace] [min price] [max price]
```

Please note that it is crucial to give a correct value for each of the selectors - all possible values are explained here:

_Version_
* all_versions
* icons
* Gold
* Gold_IF
* All Specials

_Position_
* all_positions
* Attackers
* Midfielders
* Defenders

_Nation_
* all_nations
* Brazil
* Spain
* England
* France
* Germany
* Italy
* Portugal
* Argentina

_League_
* all_leagues
* Premier_League
* LaLiga_Santander
* Serie_A
* Bundesliga
* Ligue_1

_Minimum pace_
* Any number from 1 to 99

_Minimum price_
* Any number from 0 to 15,000,000

_Maximum price_
* Any number from 0 to 15,000,000





**Start trading**



<!-- CONTRIBUTING -->
# Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Suggestions for possible **features to add** (w/o order of relevance):

* Refactor code to make it more professional
* Add any features you deem beneficial
* Update the README file to further clarify the installation and user guilde.

<!-- LICENSE -->
# License

No license.



<!-- CONTACT -->
# Contact

Alexander Nederegger - alexander@nederegger.de

Project Link: [https://github.com/alex1ned/travel_planner](https://github.com/alex1ned/travel_planner)
