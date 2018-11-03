#a-) 28x28 boyutlarında içeriği 0 ve 1 olan bir matris üretiniz.
# --- my_create_m(): return result=[]28x28  içeriği 0 1 matris
#b-) A şıkkında üretilen matrisle 1 leri içeren MBR dikdörtgeni üreten fonksiyonu yazınız
# --- def my_MBR (matrix_block) 1 leri içeren en küçük dikdörtgeni değeri elde edicek
#c-) Kendisine aktarılan iki vektörün benzerliğini return eden fonksiyonu yazınız.
# --- def ... (a,b)  skaler çarpımı göndercek geri
#d-) A şıkkında yazdığınız fonksiyonu kullanarak 100 farklı matris elde edip birinci 
#üretilen ile diğerlerini karşılaştırıp(distance) yakınlığını ve benzerliğini listeleyiniz
# --- 100 tane A daki fonk çağır ordaki 100 tanesini 1. ile karşılaştır
# haftaya mnist data

import numpy as np
import matplotlib.pyplot as plt
import random as random

#soru a
def my_create_m():
    return np.random.randint(0,2,(28,28))

#soru b
def MBR_create_28_by_28_with_0_1(matris_a):
    m=matris_a.shape[0]
    n=matris_a.shape[1]
    x_min=m
    x_max=0    
    y_min=n
    y_max=0
    for i in range(m):
        for j in range(n):
            if (matris_a[i,j]==1 and x_min>i):    
                x_min=i                          
            if (matris_a[i,j]==1 and x_max<i):
                x_max=i
            if (matris_a[i,j]==1 and y_min>j):
                y_min=j
            if (matris_a[i,j]==1 and y_max<j):
                y_max=j
    return (x_min,x_max,y_min,y_max)

#soru c
def get_similarity(character_a,character_b):
    m=character_a.shape[0]
    n=character_a.shape[1]
    my_similarity=0
    for i in range(m):
        for j in range(n):
            my_similarity=my_similarity+character_a[i,j]*character_b[i,j] 
    return my_similarity

#soru d
def get_similarity_for_100_characters(kac_karakter=100):
    characters=[]
    for i in range(kac_karakter):
        new_char=my_create_m()
        characters.append(new_char)
    for i in range(kac_karakter):
        benzerlik=get_similarity(characters[0],characters[i])
        print("0 -- "+str(i)+"  ",benzerlik)




print(my_create_m())
print(MBR_create_28_by_28_with_0_1(my_create_m()))
c_1=my_create_m()
c_2=my_create_m()
print(get_similarity(c_1,c_2))



#d şıkkı versiyon 2
a=my_create_m()
benzerlik_max=0
c=np.zeros((28,28))
for i in range(100):
    b=my_create_m()
    if(get_similarity(a,b)>benzerlik_max):
        benzerlik_max=get_similarity(a,b)
        c=b
        
print("En Yüksek Benzerlik : ",benzerlik_max)
plt.imshow(a,interpolation='nearest',cmap='gray')
plt.show()
plt.imshow(c,interpolation='nearest',cmap='gray')
plt.show()
    
get_similarity_for_100_characters()