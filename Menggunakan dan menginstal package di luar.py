import numpy as np
from PIL import Image

a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])

im = Image.open("braw.jpg")

print("format file: "+ im.format)
print("ukuran file: "+ str(im.size))
print("mode file: "+ im.mode)

im.show()
print('a:', a)
print('b:', b)
print(a+b)
