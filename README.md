# Pyfootballscoring

A utility package for managing a american football game, including scoring, down, distance and so on, Game Clock and game setup with team names and logos. Can be used for further implementation like livetickers or displaying scoreboards.

## Getting Started
This package is developed with Python3 and was not tested with Python2, so there's no guarantee it will work under Python2.

### Installation
The package can be installed by pip:
```
pip install footballscoring
```
This installs the only requirement, Apscheduler, with it.

### Testing
Run unittests simply like this while in the main directory:
```
python -m unittest discover
```

## Usage
For keeping track of the Score, Down etc. or the Game Clock, simply import the according class and instantiate it. 

### Game Clock Example 
If you want to use the Game Clock, simply instantiate the GameClock object with the required quarter length in minutes. If you want to specify the interval in which the clock should be updated, you can specify this by specifying ```interval_ms``` in milliseconds.
```python
from footballscoring.gameclock import GameClock
game_clock = GameClock(quarter_length=12, interval_ms=10)
```
Now you can simply start, stop, set or reset the clock by calling the according method.
```python
game_clock.start()
game_clock.stop()
game_clock.reset_clock()
game_clock.set_clock(minutes=2, seconds=3)
```
While creating and running the game, the package will keep track of the current game status and its validity regarding range of the values.

## Contributing
Feel free to suggest more tests or features in the Issue Section or put it as a pull request.
