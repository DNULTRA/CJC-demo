from PIL import Image

import numpy as np
x = 2
img = Image.open('lena.jpg')
im=img
iTr2=Image.new('RGB',(487,487),(255,255,255))

a = img.size[0]
b = img.size[1]
lena3 = img.resize((3*a, 3*b),Image.ANTIALIAS)
lena2_array = np.array(iTr2)
im_array = np.array(im)

for j in range(a):
    for i in range(b):

        if j >=x:
            lena2_array[i,j] = im_array[i,j-x]
        else:
            lena2_array[i,j] = (255,255,255)
lena2=Image.fromarray(np.uint8(lena2_array))
#img.save("lena3.jpg")
lena3.show()
#img.save("lena2.jpg")
lena2.show()