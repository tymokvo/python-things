from PIL import Image
import PIL.ImageOps as ops
import numpy as np

folder = '/home/tyler/Pictures/'
path = '/home/tyler/Pictures/turtle_2018-02-12_223203.png'

im = Image.open(path)

im = np.asarray(im)

out = im[:, :, 3]

# pixel_data = im.load()

# for x in range(im.size[0]):
#     for y in range(im.size[1]):
#         data = pixel_data[x, y]
#         data = list(data)
#         if data[3] > 0:
#             v = data[3]
#             pixel_data[x, y] = (v, v, v, 255)
#         else:
#             pixel_data[x, y] = (255, 255, 255, 255)

im = Image.fromarray(out)
im = ops.invert(im)
# im = im.convert('RGB')
print(im.mode)
im.save(folder + 'thepng.png')
