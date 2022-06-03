# Udacity Data Structures & Algorithms Nanodegree - Project 4 - Route Planner
This is the fourth project of the Udacity Data Structures & Algorithms Nanodegree. This project comes at the end of the 
Advanced Algorithms section, which covers:
1. Greedy Algorithms
2. Graph Algorithms 
3. Dynamics programming
4. A* Search Algorithm

## File Descriptions
The primary file in this repo is the [student_code.py](student_code.py), which contains the A* search algorithm used to 
plan the route between the given intersections. Please the docstrings within that file for a detailed description of the 
code.    
Note only does this file contain the `shortest_path` function, which is the primary route planner function, but it also 
contains unit tests.

The required tests within [test.py](test.py) also rely on the functions within [helpers.py](helpers.py) and the map 
defined within [map-40.pickle](map-40.pickle). [map-10.pickle](map-10.pickle) is a simpler test used for debugging and 
unit testing, since the required answers are easy to determine manually. All of these 4 files were provided as-is from 
Udacity except for [helpers.py](helpers.py). This file had to be updated to allow for non-notebook execution. 

## Setup Python Virtual Environment (VENV)

### Install Base Python v3.6.3 Interpreter
To start we assume that the base Python v3.6.3 interpreter is installed and is in the Path. If not, please install the v3.6.3 interpreter from [here](https://www.python.org/).     
The reason for the very old verion of Python is the map pickle files were create with a very old version of Python and NetworkX.


### Create Virtual Environment
If you are not familiar with Python Virtual Environments, please see the tutorial [here](https://docs.python.org/3/tutorial/venv.html). 
The Powershell commands are executed from within the repo's root folder, and assumes Python is installed in 
`C:\Python3.9.13`.  Linux and other shell commands are very similar.
```shell
C:\Python3.9.13\python.exe -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## References
https://www.udacity.com/course/data-structures-and-algorithms-nanodegree--nd256
https://review.udacity.com/#!/rubrics/2499/view
https://www.python.org/
https://docs.python.org/3/tutorial/venv.html
