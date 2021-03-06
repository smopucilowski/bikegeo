from ..common import geometry_to_points, points_to_tubes, points_to_cockpit

#______________________________________________________________________________
def import_2010():
    from .year_2010 import sizes, geometry
    out = dict()
    for index, size in enumerate(sizes):
        geo       = {k:v[index] for k,v in geometry.items()}
        points    = geometry_to_points(geo)
        out[size] = {
            'points':   geometry_to_points(geo),
            'tubes':    points_to_tubes(points),
            'cockpit':  points_to_cockpit(points),
        }
    return out

#______________________________________________________________________________
def _import():
    return {
        2010: import_2010(),
    }
