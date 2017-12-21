# CS410 Project: Use BM25 to improve search of gaming database from igdm.com
IGDM.com provides a searchable database of over 70,000 games.  They also provide free API access.  Currently, they implemented their search strictly on matching words in their subject lines.  The goal of this project is to expand their search capability to allow efficiently searching content by utilizing the algorithms and techniques from the cs410 course.

## Overview
The project consists of two parts - collection and search.  In collection phase, REST api from igdm.com is used to generate a games.dat file which consists of information about 1000+ games from the site.  Due to their restriction on the number of api calls made, I had to limit the number of games to aroudn 1300 games. In search phase, metapy and Python3 is used to implement a BM25 search of documents collected in games.dat.

## Implementation


## Usage

## Team Members
Kevin Kang
2) Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement
3) Documentation of the usage of the software including either documentation of usages of APIs or detailed instructions on how to install and run a software, whichever is applicable
4) Team Members

## Built With
* [metaPy](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [github](https://maven.apache.org/) - Dependency Management
* [Python3](https://rometools.github.io/rome/) - Used to generate RSS Feeds
