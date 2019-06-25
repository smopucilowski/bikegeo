import matplotlib.pyplot as plt
from numpy import cos, sin, pi, linspace, array, radians
from numpy.linalg import norm
from contextlib import contextmanager

#______________________________________________________________________________
def draw_line(a, b, *colour):
    plt.plot(
        [a[0], b[0]],
        [a[1], b[1]],
        *colour
    )

#______________________________________________________________________________
def draw_circle(centre, radius, *args):
    xs = [centre[0] + radius*cos(t) for t in linspace(0, 2*pi)]
    ys = [centre[1] + radius*sin(t) for t in linspace(0, 2*pi)]
    plt.plot(
        xs,
        ys,
        *args
    )

#______________________________________________________________________________
def draw_tubes(tubes, colour):
    for tube, parameters in tubes.items():
        draw_line(
            parameters['from'],
            parameters['to'],
            colour or parameters['plotting'],
        )

#______________________________________________________________________________
def draw_wheels(points, wheels):
    if type(wheels) is bool:
        radius = 622./2. # 700c wheel radius
        colour = 'grey'
    if type(wheels) is float:
        radius = wheels/2.
        colour = 'grey'
    if type(wheels) is tuple:
        diameter, colour = wheels
        radius = diameter/2.

    draw_circle(points['rear axle'], radius, colour)
    draw_circle(points['front axle'], radius, colour)

#______________________________________________________________________________
def draw_cranks(points, cranks):
    if type(cranks) is tuple:
        crank_arm_length, colour = cranks
    else:
        crank_arm_length = cranks
        colour = 'grey'
    draw_circle(points['bottom bracket'], crank_arm_length, colour)

#______________________________________________________________________________
def draw_cockpit(cp, cockpit):
    stem_length, stem_angle, spacer = cockpit
    stem_unit_vector = array([
        cos(-radians(stem_angle) + 3*pi/2) * cp['cockpit vector'][0]
        - sin(-radians(stem_angle) + 3*pi/2) * cp['cockpit vector'][1],
        sin(-radians(stem_angle) + 3*pi/2) * cp['cockpit vector'][0]
        - cos(-radians(stem_angle) + 3*pi/2) * cp['cockpit vector'][1],
    ])
    # rise
    draw_line(
        cp['cockpit'],
        cp['cockpit'] + spacer * cp['cockpit vector'],
    )
    # stem
    draw_line(
        cp['cockpit'] + spacer * cp['cockpit vector'],
        cp['cockpit'] + spacer * cp['cockpit vector'] + stem_length * stem_unit_vector
    )

#______________________________________________________________________________
def draw_bike(bike, colour=None, wheels=None, cockpit=None, cranks=None):
    points    = bike['points']
    draw_tubes(bike['tubes'], colour)
    if wheels:
        draw_wheels(bike['points'], wheels)
    if cranks:
        draw_cranks(bike['points'], cranks)
    if cockpit:
        draw_cockpit(bike['cockpit'], cockpit)

#______________________________________________________________________________
@contextmanager
def canvas(filename=''):
    plt.axis('equal')
    yield
    if filename:
        plt.savefig(filename)
    else:
        plt.show()
