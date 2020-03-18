# Conway's Game Of Life

## Executing the program : 

To run the provided pattern initializations with the least hassle, simply run `python3 user_input.py` in a terminal.
If you want to experiment a little more with the initial pattern and simulation settings, have a look at `sample.py`.

## Description of files

- `simulate.py`  	: Contains the class definition for the simulation.

- `patterns.py` 	: Contains famous patterns that can be placed on the grid at specific locaitons using the `GameOfLife.GameOfLife()` method.

- `initializations.py` : Contains initializations formed by combining one or more patterns from `patterns.py` that act as useful demonstrations of the program. Can be applied using the `ApplyInitialization()` method in `utils.py`.

- `utils.py` : Contains helper functions. Currently contains only `ApplyInitialization()` method.

- `sample.py` : Provides an example of using the `GameOfLife` class to run a simulation. Simulation initializations can be chosen from `initializations.py`.

- `user_input.py` : Contains a user friendly but less configurable python script that encapsulates `sample.py`. Can be used directly from the terminal.

- `config.json` : Contains the default simulation parameters.

- `/gifs` : Directory containing gifs corrspnding to the initializations in `initializations.py`.

- `/videos` : Directory containing videos corrspnding to the initializations in `initializations.py`.


## Implemented shapes :
- Block
- BeeHive
- Loaf
- Boat
- Tub
- Blinker
- Toad
- Beacon
- Pulsar
- Glider
- HeavySpaceship
- GosperGun
- Diehard
- Acorn
- Engine1


## Program outputs : 

- Initialization0 : StillLife
  ![](/gifs/gif_0.gif)

- Initialization1 : Oscillators
 ![](/gifs/gif_1.gif)
 
- Initialization2 : AcornSpread
 ![](/gifs/gif_2.gif)
 
- Initialization3 : EngineSpread
 ![](/gifs/gif_3.gif)
 
- Initialization4 : Guns
 ![](/gifs/gif_4.gif)
 
- Initialization5 : Pulsars
 ![](/gifs/gif_5.gif)
 
- Initialization6 : ShipsSimple
 ![](/gifs/gif_6.gif)
 
- Initialization7 : ShipsCollision
 ![](/gifs/gif_7.gif)
 
- Initialization8 : ShipsDestroyed
 ![](/gifs/gif_8.gif)

