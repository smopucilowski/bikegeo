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

    # Axles
    points['rear axle'] = a([
        -sqrt(geo['chain stay length']**2 - geo['bottom bracket drop']),
        geo['bottom bracket drop'],
    ])
    points['front axle'] = a([
        points['rear axle'][0] + geo['wheelbase'],
        points['rear axle'][1],
    ])

    # Head tube
    points['head tube top'] = a([
        geo['reach'],
        geo['stack'],
    ])
    points['head tube bottom'] = a([
        cos(radians(geo['head tube angle'])) * geo['head tube length'] + geo['reach'],
        - sin(radians(geo['head tube angle'])) * geo['head tube length'] + geo['stack'],
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
        'seatpost':         points['seat tube top'],
        'seatpost vector':  (points['seat tube top'] - points['seat tube bottom']) / \
                            norm(points['seat tube top'] - points['seat tube bottom']),
    }
