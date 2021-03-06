# -*- coding: utf-8 -*-
"""TTS_DE FIX FIX.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CxQZelWhkyo1gMlyKV8tk2gHgVcuiz7z
"""

#KASUS 1 DIFFERENTIAL EVOLUTION DENGAN POPULASI 20
#DE bersifat uniform 
import random

N = 20
induk  = [0 for i in range(N)]  
print(induk)

def hitungFitness(x):
    y = 15*x - x**2 
    return y

CR = 0.7  # probabilitas crossover
Pm = 0.01  # probabilitas permutasi 
BA = 100  # batas atas
BB = 0  # batas bawah

# 1. Inisialisasi (Membangkitkan populasi awal)
# untuk membuat populasi, si DE ini ada rumus ->  a = random.random() * (BA + BB) + BB
for i in range(N):  # kenapa di "for" karena N = 20
    a = random.random() * (BA + BB) + BB
    induk[i] = a
print(induk) 

epochs = 50 #menentukan berapa kali train
MaxFitness = [0 for i in range(epochs)]
# untuk populasi yang ke-0 kita hitung MaxFitness
for i in range(N):
    if (hitungFitness(induk[i]) > MaxFitness[0]):
        MaxFitness[0] = hitungFitness(induk[i])
print(induk)
print(MaxFitness)


ctr = 1
D = 1  
while ctr <  epochs:
    # 2. Seleksi
    # melakukan seleksi berdasarkan besar populasi
    for i in range(N):  # looping sebanyak jumlah populasi
        jrand = int(random.random() * D)  #memastikan bahwa akan melakukan mutasi
        for j in range(D):
            # 3. Reproduksi (Melakukan Crossover dan Permutasi)
            if (random.random() <= CR or jrand == j):
                # melakukan mutasi
                # kita akan memilih sebuah induk secara acak untuk mutasi
                xr = induk[random.randint(0, (N-1))]
                anak = xr + Pm * (induk[i])
            else:
                anak = induk
        # 4. Elitism
        if (hitungFitness(anak) >= hitungFitness(induk[i])):
            induk[i] = anak
    # end for i
    print(induk)
    for i in range(N):
        if (hitungFitness(induk[i]) > MaxFitness[ctr]):
            MaxFitness[ctr] = hitungFitness(induk[i])
    ctr += 1

# 5. Output
import matplotlib.pyplot as plt
x = range(epochs)
plt.plot(x, MaxFitness)
print('Nilai Max: ', MaxFitness[49])

#KASUS 2 DIFFERENTIAL EVOLUTION DENGAN POPULASI 100
#DE bersifat uniform 
import random

N = 100
induk  = [0 for i in range(N)]  
print(induk)

def hitungFitness(x):
    y = 15*x - x**2  
    return y

CR = 0.7  # probabilitas crossover
Pm = 0.01  # probabilitas permutasi 
BA = 100  # batas atas
BB = 0  # batas bawah

# 1. Inisialisasi (Membangkitkan populasi awal)
# untuk membuat populasi, si DE ini ada rumus -> a = random.random() * (BA + BB) + BB
for i in range(N):  # kenapa di "for" karena N = 100
    a = random.random() * (BA + BB) + BB
    induk[i] = a
print(induk) 

epochs = 50 #menentukan berapa kali training
MaxFitness = [0 for i in range(epochs)]
# untuk populasi yang ke-0 kita hitung MaxFitness
for i in range(N):
    if (hitungFitness(induk[i]) > MaxFitness[0]):
        MaxFitness[0] = hitungFitness(induk[i])
print(induk)
print(MaxFitness)


ctr = 1
D = 1  
while ctr <  epochs:
    # 2. Seleksi
    # melakukan seleksi berdasarkan besar populasi
    for i in range(N):  # looping sebanyak jumlah populasi 
        jrand = int(random.random() * D)  #memastikan bahwa akan melakukan mutasi
        for j in range(D):
            # 3. Reproduksi (Melakukan Crossover dan Permutasi)
            if (random.random() <= CR or jrand == j):
                # melakukan mutasi
                # kita akan memilih sebuah induk secara acak untuk mutasi
                xr = induk[random.randint(0, (N-1))]
                anak = xr + Pm * (induk[i])
            else:
                anak = induk
        # 4. Elitism
        if (hitungFitness(anak) >= hitungFitness(induk[i])):
            induk[i] = anak
    # end for i
    print(induk)
    for i in range(N):
        if (hitungFitness(induk[i]) > MaxFitness[ctr]):
            MaxFitness[ctr] = hitungFitness(induk[i])
    ctr += 1

# 5. Output
import matplotlib.pyplot as plt
x = range(epochs)
plt.plot(x, MaxFitness)
print('Nilai Max: ', MaxFitness[49])