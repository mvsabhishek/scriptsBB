import numpy as np
import sys
mcubes_path = r"/usr/local/lib/python3.5/dist-packages/"
if not mcubes_path in sys.path:
    sys.path.append(mcubes_path)


import mcubes
import json
data = json.load(open('/home/blender/scripts/data.json'))


# Create a data volume 
x, y, z = np.mgrid[:int(data["x"])*np.pi, :int(data["x"])*np.pi, :int(data["x"])*np.pi]
u = np.sin(x)*np.sin(y)*np.sin(z)+np.sin(x)*np.cos(y)*np.cos(z) + np.cos(x)*np.sin(y)*np.cos(z) + np.cos(x)*np.cos(y)*np.sin(z)

#Extract the 0-isosurface
verts, tri = mcubes.marching_cubes(u, 0)

mcubes.export_mesh(verts, tri, str(data["collada"]), str(data["objectName"]))


