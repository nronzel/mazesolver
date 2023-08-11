# mazesolver

## Description

Mazesolver generates a maze and then solves the maze with a depth first search
algorithm.

Written in Python and uses Tkinter for the GUI.

Python version 3.10.7

## Usage

Clone this repository to a local directory

```shell
git clone https://github.com/nronzel/mazesolver.git
```

Move into the directory, and run `main.py`
```
cd mazesolver

python main.py
```

### Changing Parameters

If you want to change the parameters of the maze, you can edit `main.py`
and change the amount of columns and rows, and the margin.

### Tests

You can run the tests with
```shell
python tests.py -v
```

## Potential Improvements

- Modify the size of the maze in GUI
- Set the speed it solves the maze in GUI
- Create a BFS algorithm to solve instead of DFS
