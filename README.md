# Battleships

Battleships is usually a two-player game, where each player has a fleet and an ocean (hidden from the other player), and tries to be the first to sink the other player's fleet. I'll just do a solo version, where the computer places the ships, and the human attempts to sink them.

The Ocean is a field of 10 x 10 squares. The squares are numbered from 0 to 9 in each dimension with numbers increasing from top to bottom and from left to right.

The fleet consists of 10 ships. The fleet is made up of 4 different types of ships, each of different size as follows:

- One battleship, occupying 4 squares
- Two cruisers, each occupying 3 squares
- Three destroyers, each occupying 2 squares
- Four submarines, each occupying 1 square

To begin the game, the computer places all the 10 ships of the fleet in the ocean randomly. Each ship can be placed either horizontally or vertically. Moreover, no ships may be immediately adjacent to each other, either horizontally, vertically, or diagonally.

The human player does not know where the ships are. The human player tries to hit the ships, by calling out a row and column number. The computer responds with one bit of information "You have a hit!" or "You missed!". When a ship is hit but not sunk, the program does not provide any information about what kind of a ship was hit. However, when a ship is hit and sinks, the program prints out a message  "You sank a  _ship-type_!".

We represent a fleet by means of a list [ship1, ship2, ....] of ships.

This projects contains all the tests needed for functions used in the implementation, the implementation, and an extension file, which provides a visualisation of the game.
