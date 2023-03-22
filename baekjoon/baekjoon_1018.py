M = int(input("M(8<=M<=50) : "))
N = int(input("N(8<=N<=50) : "))

count = 0
black_count = 0
white_count = 0
chessboard = []
new_chessrow = ""
chessrow = ""
have_to_color = 0

for i in range(M):
    new_chessrow = input()
    new_chessrow = new_chessrow.upper()
    chessrow = new_chessrow + chessrow

chessboard = list(chessrow)

for i in range(len(chessboard)):
    if chessboard[i] == "B":
        black_count = black_count + 1
    elif chessboard[i] == "W":
        white_count = white_count + 1
    else:
        continue

if black_count < 32:
        have_to_color = 32-black_count
else:
    if white_count < 32:
        have_to_color = 32-white_count


print(black_count, white_count, have_to_color)