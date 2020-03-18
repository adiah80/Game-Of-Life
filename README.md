
## Description of files

- simulate.py  	: Contains the class definition for the simulation.

- patterns.py 	: Contains famous patterns that can be placed on the grid at specific locaitons using the `GameOfLife.GameOfLife()` method.

- initializations.py : Contains initializations formed by combining one or more patterns from `patterns.py` that act as useful demonstrations of the program. Can be applied using the `ApplyInitialization()` method in `utils.py`.

- utils.py : Contains helper functions. Currently contains only `ApplyInitialization()` method.

- sample.py : Provides an example of using the `GameOfLife` class to run a simulation. Simulation initializations can be chosen from `initializations.py`.

- user_input.py : Contains a user friendly but less configurable python script that encapsulates `sample.py`. Can be used directly from the terminal.

- config.json : Contains the default simulation parameters.

- /gifs : Directory containing gifs corrspnding to the initializations in `initializations.py`.

- /videos : Directory containing videos corrspnding to the initializations in `initializations.py`.


## Executing the program : 

To run the provided pattern initializations with the least hassle, simply run `python3 user_input.py` in a terminal.

If you want to experiment a little more with the initial pattern and simulation settings, have a look at `sample.py`.

## Program outputs : 

- Initialization0 : StillLife
- Initialization1 : Oscillators
- Initialization2 : AcornSpread
- Initialization3 : EngineSpread
- Initialization4 : Guns
- Initialization5 : Pulsars
- Initialization6 : ShipsSimple
- Initialization7 : ShipsCollision
- Initializatio80 : ShipsDestroyed

