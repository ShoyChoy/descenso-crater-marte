import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

import struct
import copy
import math

# Archivo de datos
data_file = open("cdata.bin", "rb")

# Cantidad de renglones de la imagen (INT32, 4 bytes)
data = data_file.read(4)
n_rows = int.from_bytes(data, byteorder='little')
print('Rows:', n_rows)

# Cantidad de columnas de la imagen (INT32, 4 bytes)
data = data_file.read(4)
n_columns = int.from_bytes(data, byteorder='little')
print('Columns:', n_columns)

# Escala de la imagen (metros/pixel) (FLOAT64, 8 bytes)
data = data_file.read(8)
scale = struct.unpack('d', data)
scale = scale[0]
print('Scale:', scale, 'meters/pixel')

# Datos de la imagen (arreglo de números códificados en float64, 8 bytes por cada pixel)
image_size = n_rows * n_columns
data = data_file.read(8*image_size) 

# Transforma los datos de la imagen en un arreglo de numpy
image_data = np.frombuffer(data)
image_data = image_data.reshape((n_rows, n_columns))

# Superfice en 2D
cmap = copy.copy(plt.cm.get_cmap('autumn'))
cmap.set_under(color='black')   

ls = LightSource(315, 45)
rgb = ls.shade(image_data, cmap=cmap, vmin = 0, vmax = image_data.max(), vert_exag=2, blend_mode='hsv')

fig, ax = plt.subplots()

im = ax.imshow(rgb, cmap=cmap, vmin = 0, vmax = image_data.max(), 
                extent =[0, scale*n_columns, 0, scale*n_rows], 
                interpolation ='nearest', origin ='upper')

cbar = fig.colorbar(im, ax=ax)
cbar.ax.set_ylabel('Altura (m)')

plt.title('Superficie de Marte')
plt.xlabel('x (m)')
plt.ylabel('y (m)')

plt.show()

#%%
import numpy as np

b = np.min(image_data)
print(b)

c = np.where(image_data == b)

print(c)
#%%

