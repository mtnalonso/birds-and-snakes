# Birds & Snakes

Prototype Role Playing Game


## Development
#### Requirements

- Python3
- pip

#### Installation

    $ git clone https://github.com/mtnalonso/birds-and-snakes.git
    $ cd birds-and-snakes/
    $ pip install -r requirements.txt

#### Execution

The development mode uses a client - server architecture where each client emulates a player while the server displays the game information.

###### Server

    $ python3 birds_and_snakes.py -d

###### Client

    $ python3 bas/dev/client.py

###### Commands

    > create game

    > list games

    > add people: @bird @snake #c3d7288a94b34b1090c5739eec2b8154

###### Manager

Create new sqlite database

    $ python3 birds_and_snakes.py -m create_database

## WIKI
For more information please take a look at our [wiki](https://github.com/mtnalonso/birds-and-snakes/wiki)
