```python
import numpy as np
from stl import mesh

class ModelViewer:
    def __init__(self, file_path):
        self.file_path = file_path

    def display3DModel(self):
        # Load the STL files and add the vectors to the plot
        your_mesh = mesh.Mesh.from_file(self.file_path)
        figure = plt.figure()
        axes = mplot3d.Axes3D(figure)

        # Add the vectors to the plot
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        # Auto scale to the mesh size
        scale = your_mesh.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)

        # Show the plot to the screen
        plt.show()
```