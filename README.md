# Overview 
After watching team USA win the gold medal at the olympics this summer I was left without any more basketball to watch and thus I decided to create a fun project that combined my love of hoops with programming. Thus my NBA champion predictor was born. This program takes fetchs data from the nba api and saves it as a CSV file. The data is then analyzed and the 2 finalist teams are predicted based on the algorithm i devised below.

# Data Set & Algorithm  
The data set I used in this program only took into account 2024 playoff data from clutch time which is "the final five minutes of the fourth quarter or overtime when the score is within five points" as described by the NBA. My choice to use this particular data set was due to the fact that the level of play in the NBA typically only goes up as the playoffs progress and often times the deciding moments of the game occur during this clutch period. 

With the data chosen, my next step was to devise an algorithim that could predict two finalists based on this data. For my alogrithim I selected four key catagories 
- Effective Field Goal Percentage (eFG%): weighted at 40%
- Defensive Rating: weighted at 30%
- Defensive Rebounds (DREB): weighted at 20%
- Turnover Percentage (TO%): weighted at 10%

The eFG gives us an adjusted field goal percentage that takes into account three point shots, this stats is weighted the highest at 40%. My reasoning for the high weight is that teams that have a higher eFG% score more points thus the team with the best eFG% will score the most.

Defensice rating was weighted the second highest due to the fact that teams with high defensive ratings will limit opponents from scoring thus giving up less points. 

Defensice Rebounds was weighted at 20% due to the fact that while not as impactful as the previous two catagories, teams the get more defensive rebounds will get more chances to score the 


# Features 
- Fetch Protein Data: Users can input a protein ID, and the app fetches the corresponding PDB file from the RCSB Protein Data Bank.
- 3D Visualization: The fetched protein structure is displayed in 3D using PyMOL, allowing for detailed examination of molecular structures.
# Requirements 
- Python 3.1
- PyMOL (Students can get free access to the educational license required to use PyMOL by signing up [here](https://pymol.org/edu/))
- 'requests' library used to fetch the PDB files
# Installation
1. Clone the repo and cd into the Backend directory
```
git clone https://github.com/Pabz-10/protein-visualizer.git
```
2. Install PyMOL
3. Install the requests library
```
pip install requests
```
# Usage 
To run the program, make sure you're in the Backend directory and enter the command below in the terminal
```
python protein_visualization.py
```
# License
This project is licensed under the [MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) License.
