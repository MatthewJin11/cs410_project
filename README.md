# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

Project Documentation:

1) 

Given a current NBA player as input, my code will suggest the top trades associated with that player. To keep it simple, my system only considers one for one trades. I believe my code can be used as the foundation for trades in the NBA. By combining the needs of your team and the list of players from my code, a general manager will know the exact right trade for his/her team. 

2) 

My software is influenced by the vector space model we learned during lecture. THe basic idea is to project every NBA player into the vector space. The dimensions of this vector space takes into account the following normalized statistics: Salary, Points Per Game, Assists Per Game, Rebounds Per Game, Steals Per Game, Blocks Per Game, Effective Field Goal Percentage, and Three-Point Percentage. After experimenting with many features, I have found these statistics to be the most effective in finding the suitable players for a trade. Now that the every player is associated with a vector, I used cosine similarity as my similarity measure to find the most similar players to a given player. I stayed away from just finding the dot product between vectors because if I did that, then the returned players will just be the players that are good at everything. Instead, I wanted to find players that had similar salaries and production to the input player because these players would serve as good replacements. In the future, I would like to incorporate more advanced statistics and extra constraints to make my list of suggested players better. 

3) 

One of the biggest challenges of this project was finding an API to scrape basketball statistics. However, after finding out that https://www.basketball-reference.com/ is against the web scraping of their datasets, I avoided using web scrapers to scrape the most up-to-date data on the website. Instead, I manually downloaded the most recent NBA statistics (as of 12/1/2022) for the current season into two .csv files (salaries.csv and stats.csv). These two files are included in the submission as well. In the future, I hope to collaborate with the creators of basketball-reference to make my application dynamic. 

Installing and running my software is very simple and easy. My code is completely in Python. After cloning this repository, you will find a requirements.txt file for the necessary Python libraries. After installing those requirements, you can go look at the find_trades.py file for the source code. 

The command to run this script is the following: 

```python3 find_trades.py --player {player_name} --team {team abbreviation} --k {number of trade suggestions}```

For example, to find 5 players that you should trade for Russell Westbrook who is on the Los Angeles Lakers is...

```python3 find_trades.py --player "Russell Westbrook" --team LAL --k 5```

You should see:

1 John Wall
2 D'Angelo Russell
3 Jrue Holiday
4 CJ McCollum
5 Kyle Lowry

4) 

I worked alone on this project, and I can confidently say I have put in at least 20 hours for this project. This includes doing a quantitative analysis on the returned results, and I will share my thoughts on the results in the presentation video. 