import numpy as np
import os
cwd = os.getcwd()
cwd
os.chdir("C:\\imageProcessing2018")
import matplotlib.pyplot as plt
import numpy as np
im1=plt.imread("1.jpg")
plt.imshow(im1)
plt.show()
im1.setflags(write=1) 
get_ipython().run_line_magic('matplotlib', 'inline')





def get_distance(v,w=[1/3,1/3,1/3]):  
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    #d=((a*w1)**2+(b*w2)**2+(c*w3)**2)**.5 #sqrt işlemi var
    d=((a**2)*w1+(b**2)*w2+(c**2)*w3)**.5
    return d





my_RGB=[1,2,3]
gray_level=get_distance(my_RGB)
print(gray_level)





my_RGB=[10,20,3]
gray_level=get_distance(my_RGB,[.6,.3,.1])
print(gray_level)




def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            im_2[i,j]=get_distance(im_1[i,j,:])
    return im_2




im2=convert_rgb_to_gray_level(im1)
type(im2)
im1.shape,im2.shape





plt.imshow(im2,cmap='gray')
plt.show()





def convert_rgb_to_BW(image_gray_level):
    m=image_gray_level.shape[0]
    n=image_gray_level.shape[1]
    im_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if image_gray_level[i,j]>120:
                im_bw[i,j]=1
            else:
                im_bw[i,j]=0
    return im_bw





im3=convert_rgb_to_BW(im2)





plt.subplot(1,3,1),plt.imshow(im1)
plt.subplot(1,3,2),plt.imshow(im2,cmap='gray')
plt.subplot(1,3,3),plt.imshow(im3,cmap='gray') 





plt.imshow(im3,cmap='gray')
plt.show()