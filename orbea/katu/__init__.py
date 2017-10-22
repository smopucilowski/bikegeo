from ..common import geometry_to_points, points_to_tubes, points_to_cockpit

#______________________________________________________________________________
def import_2018():
    from .year_2018 import geometry
    points = geometry_to_points(geometry)
    return {
        'points':   points,
        'tubes':    points_to_tubes(points),
        'cockpit':  points_to_cockpit(points),
    }

#______________________________________________________________________________
def _import():
    return {
        2018: import_2018(),
    }
