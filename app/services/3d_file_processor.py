```python
import numpy as np
from stl import mesh

def process3DFile(file_path, infill_percentage):
    # Load the STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(file_path)

    volume, cog, inertia = your_mesh.get_mass_properties()
    weight = volume * infill_percentage

    # Calculate dimensions
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(your_mesh)
    x_dim = maxx - minx
    y_dim = maxy - miny
    z_dim = maxz - minz

    return weight, x_dim, y_dim, z_dim

def find_mins_maxs(obj):
    minx = maxx = miny = maxy = minz = maxz = None
    for p in obj.points:
        # p contains (x, y, z)
        if minx is None:
            minx = p[stl.Dimension.X]
            maxx = p[stl.Dimension.X]
            miny = p[stl.Dimension.Y]
            maxy = p[stl.Dimension.Y]
            minz = p[stl.Dimension.Z]
            maxz = p[stl.Dimension.Z]
        else:
            maxx = max(p[stl.Dimension.X], maxx)
            minx = min(p[stl.Dimension.X], minx)
            maxy = max(p[stl.Dimension.Y], maxy)
            miny = min(p[stl.Dimension.Y], miny)
            maxz = max(p[stl.Dimension.Z], maxz)
            minz = min(p[stl.Dimension.Z], minz)
    return minx, maxx, miny, maxy, minz, maxz
```