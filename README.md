# CS410 Project: Use BM25 to improve search of gaming database from igdm.com
IGDM.com provides a searchable database of over 70,000 games.  They also provide free API access.  Currently, they implemented their search strictly on matching words in their subject lines.  The goal of this project is to expand their search capability to allow efficiently searching content by utilizing the algorithms and techniques from the cs410 course.

## Overview
The project consists of two parts - collection and search.  In collection phase, REST api from igdm.com is used to generate a games.dat file which consists of information about 1000+ games from the site.  Due to their restriction on the number of api calls made, I had to limit the number of games to aroudn 1300 games. In search phase, metapy and Python3 is used to implement a BM25 search of documents collected in games.dat.

## Implementation
In collection phase, generate_gamedata.py uses REST calls to https://api-2445582011268.apicast.io/games/. Sicne I knew that the site had more than 70,000 games, I generated random numbers from 1 to 50000 to be used as game id to pass on as part of the REST call.  The site does require a api key which can be obtained from https://api.igdb.com/ by registering an account.  They allow a limited number of calls per month, and my key specified in geenrate_gamedata.py has reached the limit for the month of December, 2017.
In search phase, search_game.py utilizes metapy library to created an inverted index to be used with BM25 search algorithm.  The program will take an argument of a search term which can be multiple strings such as "dungeon master", "rpg shooter", etc.  The program will then list top five document id's that from the documents in games.dat along with some stats such as total number of documents, total number of unique terms, etc.

## Usage
* To gather a fresh set of game data from igdb.com, type "generate_gamedata.py" after updating the api_key
* To perform a search top five games that match a given search term, type "search_game.py <search term>"

## Team Members
Kevin Kang

## Built With
* [metaPy](https://github.com/meta-toolkit/metapy) - a modern data sciences toolkit
* [github](https://github.com//) - Version Control
* [Python3](https://www.python.org/) - Programming Language
