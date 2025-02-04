import pygame
import os

b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_king= pygame.image.load(os.path.join("img", "black_king.png"))
b_queen= pygame.image.load(os.path.join("img", "black_queen.png"))
b_rook= pygame.image.load(os.path.join("img", "black_rook.png"))
b_knight= pygame.image.load(os.path.join("img", "black_knight.png"))
b_pawn= pygame.image.load(os.path.join("img", "black_pawn.png"))

w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))

b = [b_bishop, b_king, b_queen, b_rook, b_pawn, b_knight]
w = [w_bishop, w_king, w_queen, w_rook, w_pawn, w_knight]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (55, 55)))

for img in w:
    W.append(pygame.transform.scale(img, (55, 55)))

class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]


    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False

    def move(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, win):
        if self.color == "w":
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]

        x = 5 + round(self.startX + (self.col * self.rect[2] / 8))
        y = 5 + round(self.startY + (self.row * self.rect[2] / 8))
        
        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 55, 55))


        win.blit(drawThis, (x, y))

class Bishop(Piece):
    img = 0

class King(Piece):
    img = 1

class Queen(Piece):
    img = 2

class Rook(Piece):
    img = 3

class Pawn(Piece):
    img = 4

class Knight(Piece):
    img = 5



