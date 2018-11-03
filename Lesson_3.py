import os
cwd = os.getcwd()
cwd
os.chdir("C:\\imageProcessing2018")
import matplotlib.pyplot as plt
import numpy as np
im_1=plt.imread("1.jpg")
plt.imshow(im_1)
plt.show()
from scipy import stats
from scipy.stats import iqr
from scipy.stats import skew
#mean=sum(img)/len(img)
#plt.subplot(1,2,2),plt.imshow(255-img)
im_1.setflags(write=1) # resim sadece read-only özelliğine sahipti üzerinde değişiklik yapabilmek için değiştirdim
im_1.flags


im_1[:,:,0]=im_1[:,:,0]+150  # resim üzerinde kırmızı tonu için renk değişimi
plt.imshow(im_1)
plt.show()


def my_function(x):
    return 255-x

def inverse(image):
    image[:,:,0]=my_function(image[:,:,0])
    image[:,:,1]=my_function(image[:,:,1])
    image[:,:,2]=my_function(image[:,:,2])
    
def mean(image):
    print("Kirmizi icin renk ortalamasi : ",np.mean(image[:,:,0]))
    print("Yesil icin renk ortalamasi : ",np.mean(image[:,:,1]))
    print("Mavi icin renk ortalamasi : ",np.mean(image[:,:,2]))
    
def median(image):
    print("Kirmizi icin renk ortanca degeri : ",np.median(image[:,:,0]))
    print("Yesil icin renk ortanca degeri : ",np.median(image[:,:,1]))
    print("Mavi icin renk ortanca degeri : ",np.median(image[:,:,2]))
    
def mode(image):
    print("Kirmizi icin renk modu : ",stats.mode(image[:,:,0]))
    print("Yesil icin renk modu : ",stats.mode(image[:,:,1]))
    print("Mavi icin renk modu : ",stats.mode(image[:,:,2]))
    
    
def my_H(image):
    H={}
    for i in range (image.shape[0]):
        for j in range (image.shape[1]):
            if(image[i,j,0] in H.keys()):
                H[image[i,j,0]]=H[image[i,j,0]]+1
            else:
                H[image[i,j,0]]=1
            if(image[i,j,1] in H.keys()):
                H[image[i,j,1]]=H[image[i,j,1]]+1
            else:
                H[image[i,j,1]]=1
            if(image[i,j,2] in H.keys()):
                H[image[i,j,2]]=H[image[i,j,2]]+1
            else:
                H[image[i,j,2]]=1
    plt.bar(list(H.keys()),list( H.values()), color='r')
    plt.show()
            
                
def ceyreklik(image):
    print("Kirmizi icin Q1 degeri = ",np.percentile(image[:,:,0],25))
    print("Kirmizi icin Q2 degeri = ",np.percentile(image[:,:,0],50))
    print("Kirmizi icin Q3 degeri = ",np.percentile(image[:,:,0],75))
    print("Yesil icin Q1 degeri = ",np.percentile(image[:,:,1],25))
    print("Yesil icin Q2 degeri = ",np.percentile(image[:,:,1],50))
    print("Yesil icin Q3 degeri = ",np.percentile(image[:,:,1],75))
    print("Mavi icin Q1 degeri = ",np.percentile(image[:,:,2],25))
    print("Mavi icin Q2 degeri = ",np.percentile(image[:,:,2],50))
    print("Mavi icin Q3 degeri = ",np.percentile(image[:,:,2],75))
    print("Kirmizi icin iqr degeri = ",iqr(image[:,:,0]))
    print("Yesil icin iqr degeri = ",iqr(image[:,:,1]))
    print("Mavi icin iqr degeri = ",iqr(image[:,:,2]))
    
def ss(image):
    print("Kirmizi icin skewness degeri = ",skew(image[:,:,0]))
    print("Yesil icin skewness degeri = ",skew(image[:,:,1]))
    print("Mavi icin skewness degeri = ",skew(image[:,:,2]))
    
def aralik(image):
    print("Kirmizi icin range araligi = ",image[:,:,0].max()-image[:,:,0].min())
    print("Yesil icin range araligi = ",image[:,:,0].max()-image[:,:,1].min())
    print("Mavi icin range araligi = ",image[:,:,0].max()-image[:,:,2].min())
    

inverse(im_1)
mean(im_1)
median(im_1)
mode(im_1)
plt.imshow(im_1)
plt.show()
my_H(im_1)
ceyreklik(im_1)
ss(im_1)
aralik(im_1)