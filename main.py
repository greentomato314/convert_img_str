from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
path = r"C:\\Users\\cycli\\Downloads\\img.jpg"
img = Image.open(path)
X,Y = img.size
def encode_img(img):
    arr = np.array(img).flatten()
    return ''.join([str(i).zfill(3) for i in arr])
def decode_img(s,X,Y):
    ls = []
    for i in range(0,len(s),3):
        ls.append(int(s[i:i+3]))
    return Image.fromarray(np.array(ls).reshape(Y,X,3).astype('int8'),mode='RGB')

str1 = encode_img(img)
print(len(str1))
img2 = decode_img(str1, X, Y)
ax = plt.subplot(1,2,1)
ax.imshow(img)
ax.set_axis_off()
ax = plt.subplot(1,2,2)
ax.imshow(img2)
ax.set_axis_off()
plt.show()
