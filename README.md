# Tic-tac-toe
Tic-tac-toe game

## Requirements

- 3 x 3 grid
- User and computer play turn by turn
- The board and the moves are displayed after each turn
- Once a game is won, the winner is announced and a new game can be started

## Configuration

1. Create virtual enviroment

```
virtualenv venv
```

2. Activate virtual enviroment

Generally:

```
source venv/bin/activate
```

When using fish:

```
. venv/bin/activate.fish
```

3. Install all dependencies

**When finish, deactivate venv:**

Generally:

```
source deactivate
```

When using fish:

```
deactivate
```

## Run game

```
python2 main.py
```

And enjoy!


**Note**: I'm using python2 since there is a problem with my Mac OS, see:
`https://github.com/pygame/pygame/issues/555`

## Tests

You can find some tests in /test.

To run:

```
python2 -m pytest
```