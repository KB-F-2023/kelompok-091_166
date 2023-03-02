import numpy as np
from time import sleep

nodeDikunjungi = []
kondisiAkhir = [0, 1, 2, 3, 4, 5, 6, 7, 8]
puzzleTuntas = False
jmlNodeDikunjungi = 0

class Node:
    def __init__(self, Puzzle, langkah):
        self.Puzzle = Puzzle
        self.langkah = langkah
    
    def __repr__(self):
        return '( ' + str(self.Puzzle) + ', ' + self.langkah + ' )'

    def __str__(self):
        return '( ' + str(self.Puzzle) + ', ' + self.langkah + ' )'

class NodeInformed:
    def __init__(self, Puzzle, langkah, nilaiF):
        self.Puzzle = Puzzle
        self.langkah = langkah
        self.nilaiF = nilaiF
    
    def __repr__(self):
        return '( ' + str(self.Puzzle) + ' | ' + self.langkah + str(self.nilaiF) + ' )'

    def __str__(self):
        return '( ' + str(self.Puzzle) + ' | ' + self.langkah + str(self.nilaiF) + ' )'

# heuristic 1: salah penempatan
def h1(Puzzle):
    salahTempat = 9 - sum(np.array(Puzzle) == np.array(kondisiAkhir))

    if Puzzle.index(0) != 4:
        salahTempat -= 1

    return salahTempat

# heuristic 2: manhattan distance
def h2(Puzzle):
    jumlah = 0

    for indeks,cek in enumerate(Puzzle):
        if (cek == 0):
            continue

        barisAwal, kolomAwal = int(indeks/3), (indeks % 3)
        indeksTujuan = kondisiAkhir.index(cek)
        barisTujuan, kolomTujuan = int(indeksTujuan/3), (indeksTujuan % 3)
        jumlah += abs(kolomTujuan - kolomAwal) + abs(barisTujuan - barisAwal)
    return jumlah

def pergerakanMungkin(Puzzle):
    kemungkinanGerak = []     
    kemungkinanGerak.append('ATAS') if (Puzzle.index(0) > 2) else 0
    kemungkinanGerak.append('BAWAH') if (Puzzle.index(0) < 6) else 0
    kemungkinanGerak.append('KIRI') if (Puzzle.index(0) % 3 > 0) else 0
    kemungkinanGerak.append('KANAN') if (Puzzle.index(0) % 3 < 2)  else 0
    return kemungkinanGerak

def gerakAtas(Puzzle):
    posisiKosong = Puzzle.index(0)
    Puzzle[posisiKosong], Puzzle[posisiKosong - 3] = Puzzle[posisiKosong - 3], Puzzle[posisiKosong]
    return Puzzle

def gerakBawah(Puzzle):
    posisiKosong = Puzzle.index(0)
    Puzzle[posisiKosong], Puzzle[posisiKosong + 3] = Puzzle[posisiKosong + 3], Puzzle[posisiKosong]
    return Puzzle

def gerakKanan(Puzzle):
    posisiKosong = Puzzle.index(0)
    Puzzle[posisiKosong], Puzzle[posisiKosong + 1] = Puzzle[posisiKosong + 1], Puzzle[posisiKosong]
    return Puzzle

def gerakKiri(Puzzle):
    posisiKosong = Puzzle.index(0)
    Puzzle[posisiKosong], Puzzle[posisiKosong - 1] = Puzzle[posisiKosong - 1], Puzzle[posisiKosong]
    return Puzzle

def gerakan(Puzzle, tipeGerakan):
    if (tipeGerakan == 'ATAS'):
        return gerakAtas(Puzzle)
    elif (tipeGerakan == 'BAWAH'):
        return gerakBawah(Puzzle)
    elif (tipeGerakan == 'KANAN'):
        return gerakKanan(Puzzle)
    elif (tipeGerakan == 'KIRI'):
        return gerakKiri(Puzzle)

def pembanding(benda):
    return benda.nilaiF

def bukaNode(daftarNode, heuristic):
    global jmlNodeDikunjungi, nodeDikunjungi
    jmlNodeDikunjungi += 1
    nodeSkrg = daftarNode.pop(0)
    pergerakan = pergerakanMungkin(nodeSkrg.Puzzle)

    for gerak in pergerakan:
        puzzleBaru = gerakan(list(nodeSkrg.Puzzle), gerak)

        if puzzleBaru in nodeDikunjungi:
            continue

        nodeDikunjungi.append(puzzleBaru)
        newNode = NodeInformed(puzzleBaru, nodeSkrg.langkah + gerak + ', ', nodeSkrg.langkah.count(',') + heuristic(puzzleBaru))
        daftarNode.append(newNode)

def selesaikan(Puzzle, heuristic):
    akar = NodeInformed(Puzzle, '', heuristic(Puzzle))
    daftarNode = [akar]

    while not puzzleTuntas:
        daftarNode = sorted(daftarNode, key=pembanding)

        if (daftarNode[0].Puzzle == kondisiAkhir):
            break

        print(daftarNode[0])
        print('\n')
        
        bukaNode(daftarNode, heuristic)

    print(daftarNode[0])
    nodeTuntas = daftarNode[0]
    nodeTuntas.langkah = nodeTuntas.langkah [:-2]
    print ('Penyelesaian: ' + nodeTuntas.langkah)
    print ('Jumlah node yang dikunjungi: ' + str(jmlNodeDikunjungi))

def masukkanArray():
    isiArray = list(map(int, input('Masukkan kondisi awal 8 puzzle: ').split()))
    return isiArray
 
def main():
    Puzzle = masukkanArray()
    selesaikan(Puzzle, h2)

if __name__ == '__main__':
    main()
