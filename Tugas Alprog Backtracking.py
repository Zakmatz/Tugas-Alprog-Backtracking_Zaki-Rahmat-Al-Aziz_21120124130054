import time

N = 4

# bikin papan kosong
board = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(".")
    board.append(row)


# fungsi tampil papan
def print_board():
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()
    time.sleep(0.5)


# cek apakah aman
def aman(baris, kolom):
    # cek kolom
    for i in range(baris):
        if board[i][kolom] == "Q":
            return False

    # cek diagonal kiri atas
    i = baris - 1
    j = kolom - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # cek diagonal kanan atas
    i = baris - 1
    j = kolom + 1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


# fungsi utama
def solve(baris):
    # kalau semua baris sudah terisi
    if baris == N:
        print("SOLUSI DITEMUKAN:")
        print_board()
        return True

    # coba setiap kolom
    for kolom in range(N):
        if aman(baris, kolom):
            print(f"Pasang Q di ({baris},{kolom})")
            board[baris][kolom] = "Q"
            print_board()

            # lanjut ke baris berikutnya
            if solve(baris + 1):
                return True

            # BACKTRACK
            print(f"Backtrack dari ({baris},{kolom})")
            board[baris][kolom] = "."
            print_board()

    return False


solve(0)