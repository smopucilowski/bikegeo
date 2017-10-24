from numpy import array as a,cos, sin, sqrt, radians
from numpy.linalg import norm

#______________________________________________________________________________
def geometry_to_points(geo):
    points = dict()

    # Bottom bracket
    points['bottom bracket'] = a([0., 0.])

    # Seat tube
    points['seat tube bottom'] = points['bottom bracket']
    points['seat tube top']    = a([
        - cos(radians(geo['seat tube angle'])) * geo['seat tube length'],
        sin(radians(geo['seat tube angle'])) * geo['seat tube length'],
    ])
    points['frame top'] = a([
        - cos(radians(geo['seat tube angle'])) * geo['frame height'],
        sin(radians(geo['seat tube angle'])) * geo['frame height'],
    ])

    # Axles
    points['rear axle'] = a([
        -sqrt(geo['chainstay length']**2 - geo['bb drop']),
        geo['bb drop'],
    ])
    points['front axle'] = a([
        points['rear axle'][0] + geo['wheelbase'],
        points['rear axle'][1],
    ])

    # Head tube
    other_angle_1 = radians(180 - geo['fork angle'])
    other_angle_2 = radians(90  - geo['fork angle'])
    points['head tube bottom'] = a([
        points['front axle'][0] + cos(other_angle_1) * geo['fork length'] - cos(other_angle_2) * geo['fork rake'],
        points['front axle'][1] + sin(other_angle_1) * geo['fork length'] - sin(other_angle_2) * geo['fork rake'],
    ])
    points['head tube top'] = a([
        points['head tube bottom'][0] + cos(other_angle_1) * geo['head tube length'],
        points['head tube bottom'][1] + sin(other_angle_1) * geo['head tube length'],
    ])

    return points

#______________________________________________________________________________
def points_to_tubes(points):
    return {
        'chainstay': {
            'from':     points['bottom bracket'],
            'to':       points['rear axle'],
            'plotting': '',
        },
        'seat tube': {
            'from':     points['seat tube bottom'],
            'to':       points['seat tube top'],
            'plotting': '',
        },
        'frame top': {
            'from':     points['seat tube top'],
            'to':       points['frame top'],
            'plotting': '',
        },
        'head tube': {
            'from':     points['head tube top'],
            'to':       points['head tube bottom'],
            'plotting': '',
        },
        'fork': {
            'from':     points['head tube bottom'],
            'to':       points['front axle'],
            'plotting': '',
        },
        'down tube': {
            'from':     points['bottom bracket'],
            'to':       points['head tube bottom'],
            'plotting': '',
        },
        'top tube': {
            'from':     points['seat tube top'],
            'to':       points['head tube top'],
            'plotting': '',
        },
        'seat stay': {
            'from':     points['seat tube top'],
            'to':       points['rear axle'],
            'plotting': '',
        },
    }

#______________________________________________________________________________
def points_to_cockpit(points):
    return {
        'cockpit':          points['head tube top'],
        'cockpit vector':   (points['head tube top'] - points['head tube bottom']) / \
                            norm(points['head tube top'] - points['head tube bottom']),
        'seatpost':         points['frame top'],
        'seatpost vector':  (points['frame top'] - points['seat tube top']) / \
                            norm(points['frame top'] - points['seat tube top']),
    }
