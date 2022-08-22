def puntosCurva(start, end, control, resolution=5):
	# If curve is a straight line
	if (start[0] - end[0])*(start[1] - end[1]) == 0:
		return [start, end]

	# If not return a curve
	path = []

	for i in range(resolution+1):
		t = i/resolution
		x = (1-t)**2 * start[0] + 2*(1-t)*t * control[0] + t**2 *end[0]
		y = (1-t)**2 * start[1] + 2*(1-t)*t * control[1] + t**2 *end[1]
		path.append((x, y))

	return path

def curvaCalle(start, end, control, resolution=15):
	points = puntosCurva(start, end, control, resolution=resolution)
	return [(points[i-1], points[i]) for i in range(1, len(points))]

IZQ = 0
DERECH = 1
def giros(start, end, vuelta, resolution=15):
	# Get control point
	x = min(start[0], end[0])
	y = min(start[1], end[1])

	if vuelta == IZQ:
		control = (
			x - y + start[1],
			y - x + end[0]
		)
	else:
		control = (
			x - y + end[1],
			y - x + start[0]
		)
	
	return curvaCalle(start, end, control, resolution=resolution)
