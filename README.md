# War Simulation

## Introduction

A python simulation of the card game war.

While playing war with my girlfriend the other day I was curious how long
the average game might last between two people. This is a quick simulation/experiment 
I am working on to get an average number of turns, and eventually get an average time.

Considering the current social distancing situation we're in on a global scale,
I figured this might be a good way to pass the time.

Cheers,

Daniel

## Procedure

### Software Requirements
This experiment was built and run with Python3. No additional packages are required to
install for the simulation, but you are going to need to install Pandas, Numpy, and 
Jupyter Notebook to run the analysis script.

### Running the Simulation
For this quick experiment I created an object oriented representation of the game
of war between two people. The source for this can be found in the `/src` file.

To run the simulation once, change into the `/src` file an run the following command

```sh
python3 main.py
```

To run the simulation any number of times, `n`, run the following command

```sh
python3 main.py [n]
```

The results of the simulation are saved into `data/game_log.csv` in the following format

```
[Total turns for the simulation],[Number of rounds of war that were played],[Which player won the game]
```

For this experiment I ran the simulation 60,000 times.

### Gathering Estimate Trial Time Data
In order to gather an estimate for time to complete a game we found a rough estimate on how
long it takes to complete a simple turn, meaning two cards are played an a winner is immediately found.
Then we found the a rough estimate on how long it takes to complete a round of war, meaning two cards are
played, are tied, then the players have to play a round of war to determine the winner. 

The breakdown of the trials are found in `data/sample_data.txt`.

### Game Analysis
After having simulation data and trial run time estimates, I used Jupyter Notebook and pandas
to build a quick table. Knowing the total turns and number of turns that were rounds of war,
I made the assumption that only one game of war would be played at a given time. In other words

```
Total Turns = Nonwar Turns + War Turns
```

Using this assumption and time estimates, I used the following equation to find an estimated game time
for each simulation

```
Total Game Time = (Nonwar Turns * Estimated Time per Simple Turn) + (War Turns * Estimated Time per War Turn)
```
After finding Estimated Total Game Time for each simulation, I used the interquartile range to remove
statistical outliers. With a collection of non-outliers, I used the average to find the average estimated
time of a game of war.

I also followed the same method of removing outliers and using the average to find the average number
of turns required to complete a game of war between two people. Just cause I had the information.

## Results

The average estimated time to complete a game of war between two people: `17.17 minutes (or 17 minutes, 10 seconds)`

The average estimated number of turns to complete a game of war between two people: `286.72 turns`
