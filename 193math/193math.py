# this program calculates the dimensions of various shapes 
# depending solely upon the volume given.  ex) if volume
# is 27 cubic meters, a cube would have sides of 3 m.

import math

volume = int(raw_input("volume in cubic meters > "))

# cubevolume = height x width x length = height ** 3
# so side = volume ** (1/3.0)

cube_side = volume ** (1/3.00)


# sphere volume = (4/3)math.pi*radius^3
# radius^3 = (3/4) * volume / math.pi

sphere_radius = (((3 / 4.0) * volume) / math.pi) ** (1/3.0)

# cylinder volume = pi * r^2 * height
# using height of the cube as height
# radius = ( Volume / (cube_side * math.pi) ) ^ (1/2.0)

cylinder_radius = (volume / (cube_side * math.pi) ) ** (1/2.0)
cylinder_diameter = 2 * cylinder_radius

# cone volume = ((3 * volume) / (pi * 3 * cube_height)) ^ (1/2.0)

cone_radius = (volume / (math.pi * cube_side)) ** (1/2.0)
cone_height = 3 * cube_side

print "Cube: %.2f m. width, %.2f m. high, %.2f m. long" % (cube_side, cube_side, cube_side)
print "Sphere: %.2f m. radius" % (sphere_radius)
print "Cylinder: %.2f m. tall, %.2f m. diameter" % (cube_side, cylinder_diameter)
print "Cone: %.2f m. tall, %.2f m. radius" % (cone_height, cone_radius)