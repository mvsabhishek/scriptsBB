"""
in bounds s d=10 n=2
in iso_val s d=8.0 n=2
in samples s d=100 n=2
out vertices v
out triangles s
"""


import numpy as np
import sys
mcubes_path = r"C:\Users\sivaabhishek\Anaconda3\envs\py35\Lib\site-packages" 
print (mcubes_path)
if not mcubes_path in sys.path:
    sys.path.append(mcubes_path)   

	
import mcubes

#def f(x, y, z):
#	return x**2 + y**2 + z**2
		
# Create a data volume (30 x 30 x 30)
X, Y, Z = np.mgrid[:10*np.pi, :10*np.pi, :10*np.pi]
u = np.cos(X) + np.cos(Y) + np.cos(Z)

#Extract the 0-isosurface
verts, tri = mcubes.marching_cubes(u, 0)

# Extract the 16-isosurface
"""verts, tri = mcubes.marching_cubes_func(
	(-bounds, -bounds, -bounds), (bounds, bounds, bounds),  # Bounds
	samples, samples, samples,              # Number of samples in each dimension
	f,                          # Implicit function
	iso_val)                         # Isosurface value
"""
#vertices, triangles = verts.tolist(), tri.tolist()
mcubes.export_mesh(verts, tri, "schwarz.dae", "SchwarzP")