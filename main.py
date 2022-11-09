import random
import sys

# class includes function, which generates board
class Board:
    def __init__(self, dimention, playerX, playerY, appleX, appleY, rockX, rockY, deathX, deathY):
        self.dimention = dimention
        self.playerX = playerX
        self.playerY = playerY
        self.appleX = appleX
        self.appleY = appleY
        self.counter = (dimention + 2)
        self.rockX = rockX
        self.rockY = rockY
        self.deathX = deathX
        self.deathY = deathY

    def drawBoard(self):
        table = [["."] * boardDimention for i in range(boardDimention)]
        table[player[0]][player[1]] = 'P'
        table[apple[0]][apple[1]] = 'O'
        table[rock[0]][rock[1]] = 'R'
        table[death[0]][death[1]] = 'D'
        self.horizontalLine()
        for rows in table:
            sys.stdout.write("|")
            for row in rows:
                sys.stdout.write(row)
            print("|")
        self.horizontalLine()

    def horizontalLine(self):
        for count in range(self.counter):
            sys.stdout.write("-")
        print(" ")

# class includes function, which generates cooridinates
class Coordinate:
    def __init__(self, dimention):
        self.dimention = dimention

    def drawCoordinate(self):
        coordinates = []
        coordinates.append(random.randint(0, boardDimention - 1))
        coordinates.append(random.randint(0, boardDimention - 1))
        return coordinates

# class return dimention board
class Level:
    def __init__(self, number, userStartDimention):
        self.number = number
        self.userDimention = (userStartDimention + 1)

    def returnDimention(self):
        return self.userDimention

def playGame():
    table.drawBoard()
    print("Gdzie chcesz przesunąć gracza? ")
    print("W górę: wciśnij W")
    print("W dół: wciśnij S")
    print("W lewo: wciśnij A")
    print("W prawo: wciśnij D")
    print("Kliknij Q aby wyjść")

def compare(firstlist, secondlist):
    if firstlist[0] != secondlist[0] or firstlist[1] != secondlist[1]:
        return True

# Start game
print("Gra polega na jak najszybszym dotarciu do jabłka (oznaczony symbole O).")
print("Staraj się uzyskać jak najmniej punktów")
print("Omijaj skały (R)")
print("Uważaj na przeszkody (D)")
print("Powodzenia :)")
while(True):
    userNumberLevel = int(input("Podaj liczbę poziomów: "))
    if userNumberLevel>0:
        break
while(True):
    userStartDimention = int(input("Podaj startowy wymiar mapy (min. 3): "))
    if userStartDimention > 2:
        break
numberLevel = 1
choice = ["A", "D", "W", "S", "Q"]
level = Level(numberLevel, userStartDimention)
boardDimention = level.returnDimention()
coordinate = Coordinate(boardDimention)
player = coordinate.drawCoordinate()
while (True):
    apple = coordinate.drawCoordinate()
    if compare(player, apple):
        break
while (True):
    rock = coordinate.drawCoordinate()
    if compare(player, rock):
        if compare(apple, rock):
            break
while (True):
    death = coordinate.drawCoordinate()
    if compare(player, death):
        if compare(apple, death):
            if compare(rock, death):
                break
table = Board(boardDimention, player[0], player[1], apple[0], apple[1], rock[0], rock[1], death[0], death[1])
result = 0

while (numberLevel <= userNumberLevel):
    if (player[0] == death[0] and player[1] == death[1]):
        print("przegrałeś :(")
        break
    elif (player[0] == apple[0] and player[1] == apple[1]):
        print("Wygrałeś")
        numberLevel += 1
        level = Level(numberLevel, userStartDimention)
        boardDimention = level.returnDimention()
        player = coordinate.drawCoordinate()
        while (True):
            apple = coordinate.drawCoordinate()
            if apple[0] != player[0] or apple[1] != player[1]:
                break
# event handling
    else:
        playGame()
        move = input("Podaj wybór:")
        result += 1
        while (move not in choice):
            move = input("Podaj wybór:")
        if (move == "A"):
            if ((player[1] -1) % boardDimention) != rock[1] or player[0] != rock[0]:
                player[1] = (player[1] - 1) % boardDimention
        elif (move == "D"):
            if ((player[1] + 1) % boardDimention) != rock[1] or player[0] != rock[0]:
                player[1] = (player[1] + 1) % boardDimention
        elif (move == "W"):
            if ((player[0] - 1) % boardDimention) != rock[0] or player[1] != rock[1]:
                player[0] = (player[0] - 1) % boardDimention
        elif (move == "S"):
            if ((player[0] + 1) % boardDimention) != rock[0] or player[1] != rock[1]:
                player[0] = (player[0] + 1) % boardDimention
        elif (move == "Q"):
            break

print("Uzyskałeś " + str(result) + "punktów")
