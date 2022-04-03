import turtle

t = turtle.Turtle()
# Orient so to draw hexes 'flat side up,' right 30 degrees, left 330 as in turtle standard mode
orientation = 330
hex_radius = 24
t.speed(0)

# define the 'coordinate system', inclusive
grid_bounds = {
    'x': (-3, 2),
    'y': (0, 2)
}

tile_colors = {
    'd': '#ffb600',
    'f': '#39b448',
    'm': '#cccccc',
    's': '#351c75',
    'w': '#4f86f7'
}

# note the tile layers will be inverted, vertically
tile_list_1 =  [['s', 's', 'd', 'd', 'd', 'f'],
                ['s', 's', 'w', 'd', 'f', 'f'],
                ['w', 'w', 'w', 'w', 'f', 'f']]

tile_list_2 =  [['s', 'm', 'm', 'm', 'm', 'd'],
                ['s', 's', 'f', 'd', 'd', 'd'],
                ['s', 'f', 'f', 'f', 'f', 'f']]

tile_list_3 =  [['m', 'm', 'm', 'm', 'w', 'w'],
                ['s', 's', 'f', 'm', 'w', 'w'],
                ['s', 's', 'f', 'f', 'f', 'w']]

tile_list_4 =  [['d', 'd', 'd', 'f', 'f', 'f'],
                ['d', 'd', 'm', 'w', 'w', 'w'],
                ['d', 'd', 'm', 'm', 'm', 'm']]

tile_list_5 =  [['d', 'd', 'w', 'w', 'w', 'w'],
                ['s', 'd', 'd', 'w', 'm', 'm'],
                ['s', 's', 's', 'm', 'm', 'm']]

tile_list_6 =  [['m', 'w', 'w', 'w', 'w', 'f'],
                ['m', 'm', 's', 's', 'f', 'f'],
                ['d', 'd', 's', 's', 's', 'f']]

# Given the index vector x = (x_target - x), y = (y_target - y),
# move the turtle for drawing next hex there.
# radius = circumradius = len_side
# part_step = apothem = inradius
def move_along_vector(x, y, radius):
    t.penup()
    x_direction = 180 if x < 0 else 0
    y_direction = 270 if y < 0 else 90
    x_step      = 1.5
    y_step      = 2
    x_steps     = abs(x)
    y_steps     = abs(y)

    if x_steps > 0:
        t.left(x_direction)
        t.forward(radius * x_step * x_steps)
        t.right(x_direction)

    if y_steps > 0:
        t.left(y_direction)
        apothem = radius * .86602540378
        part_step = 0
        if x_steps % 2:
            part_step = apothem # the apothem, or inradius, is the len_side * (sqrt(3)/2)
        t.forward(part_step)
        t.forward(apothem * y_step * (y_steps - 1))
        t.right(y_direction)
    t.pendown()

def draw_hex(radius, orientation, fill_color):
    t.fillcolor(fill_color)
    t.setheading(orientation)
    t.begin_fill()
    t.circle(radius, steps=6)
    t.end_fill()
    t.setheading(0)

# # left to right, bottom to top
def draw_grid(grid_bounds, tiles, flip=False):
    grid_start = (grid_bounds['x'][0],grid_bounds['y'][0])
    grid_extents = (grid_bounds['x'][1] - grid_bounds['x'][0], grid_bounds['y'][1] - grid_bounds['y'][0])
    print(f'grid extents: {grid_extents}')

    move_along_vector(grid_start[0], grid_start[1], hex_radius)
    if not flip:
        for i in range(grid_extents[1] + 1):
            for j in range(grid_extents[0] + 1):
                tile = tiles[i][j]
                color = tile_colors[tile]
                draw_hex(hex_radius, orientation, color)
                y_move = 1 if j % 2 else -1
                move_along_vector(1, y_move, hex_radius)
            move_along_vector(-grid_extents[0] -1, 2, hex_radius)
    else:
        for i in range(grid_extents[1], -1, -1):
            for j in range(grid_extents[0], -1, -1):
                tile = tiles[i][j]
                color = tile_colors[tile]
                draw_hex(hex_radius, orientation, color)
                y_move = -1 if j % 2 else 1
                move_along_vector(1, y_move, hex_radius)
            move_along_vector(-grid_extents[0] -1, 2, hex_radius)

draw_grid(grid_bounds, tile_list_6, True)

turtle.update()
turtle.done()