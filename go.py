from draw import draw_bike, canvas
import bmc
import salsa
import orbea

with canvas():
    draw_bike(
        bmc.roadmachine[2017][61],
        colour='black',
        wheels=True,
        cockpit=(120,-6,25),
        cranks=175,
    )
    draw_bike(
        salsa.fargo[2018]['lg'],
        wheels=True,
        cockpit=(80,6,25),
        cranks=175,
    )

with canvas():
    draw_bike(
        orbea.katu[2018],
        wheels=20*25.4,
        cranks=170,
    )
