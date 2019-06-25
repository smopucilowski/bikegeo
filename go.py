from draw import draw_bike, canvas
import bmc
import specialized

with canvas():
    draw_bike(
        bmc.roadmachine[2018][54],
        colour='black',
        wheels=True,
        cockpit=(90,-6,10),
        cranks=165,
    )
    draw_bike(
        specialized.allez_sprint[2019][54],
        wheels=True,
        cockpit=(90,-17,10),
        cranks=165,
    )

