import xml.etree.ElementTree as ET
import plotly.graph_objects as go

tree = ET.parse('cutted-box.x3d')
root = tree.getroot()
coords_input = root.find('Scene/Transform/Transform/Group/Shape/IndexedFaceSet/Coordinate').get('point').split(' ')
coords_input = coords_input[:-1]

divide = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
points = divide(coords_input, 3)

x = list()
y = list()
z = list()
for point in points:
    x.append(point[0])
    y.append(point[1])
    z.append(point[2])

x = x[3:]
y = y[3:]
z = z[3:]

mesh = go.Mesh3d(x = x, y = y, z = z, color = 'black', opacity = 0.50)
fig = go.FigureWidget(data = [mesh])
fig.show()