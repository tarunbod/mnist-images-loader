'''
=======================
From the MNIST Website:
=======================

TRAINING SET IMAGE FILE (train-images-idx3-ubyte):

[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000803(2051) magic number 
0004     32 bit integer  60000            number of images 
0008     32 bit integer  28               number of rows 
0012     32 bit integer  28               number of columns 
0016     unsigned byte   ??               pixel 
0017     unsigned byte   ??               pixel 
........ 
xxxx     unsigned byte   ??               pixel
Pixels are organized row-wise. 
Pixel values are 0 to 255.
0 means background (white), 255 means foreground (black).
'''

import numpy as np
from PIL import Image
import os

images = list()
SIZE = 28

with open('train-images.idx3-ubyte', 'rb') as imgs_file:
    imgs_file.read(16)
    for i in range(60000):
        print('Image #%s' % (i + 1), end='\r')
        new_image = np.zeros((SIZE, SIZE))
        for row in range(SIZE):
            for col in range(SIZE):
                new_image[row][col] = 255 - int.from_bytes(imgs_file.read(1), 'big')
    
        images.append(new_image)

print('Done reading images, now to write...')

if not os.path.exists('images/'):
    os.mkdir('images')

for idx, img in enumerate(images):
    print('Image #%s' % (idx + 1), end='\r')
    Image.fromarray(img).convert('RGB').save('images/mnist-image-%d.png' % idx)


print('Done.')
