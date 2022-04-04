import turtle

t = turtle.Turtle()
# Orient so to draw hexes 'flat side up,' right 30 degrees, left 330 as in turtle standard mode
orientation = 330
hex_radius = 24
t.speed(0)


tile_topo_colors = {
    'd': '#ffb600',
    'f': '#39b448',
    'm': '#cccccc',
    's': '#351c75',
    'w': '#4f86f7'
}

tile_territory_colors = {
    'b': '#000000',
    'l': '#cc0000'
}

# note the tile layers will be inverted, vertically
tile_topo_1 =          [['s', 's', 'd', 'd', 'd', 'f'],
                        ['s', 's', 'w', 'd', 'f', 'f'],
                        ['w', 'w', 'w', 'w', 'f', 'f']]
tile_territories_1 =   [[' ', ' ', ' ', 'b', 'b', 'b'],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ']]


tile_topo_2 =          [['s', 'm', 'm', 'm', 'm', 'd'],
                        ['s', 's', 'f', 'd', 'd', 'd'],
                        ['s', 'f', 'f', 'f', 'f', 'f']]
tile_territories_2 =   [[' ', ' ', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' '],
                        ['l', 'l', 'l', ' ', ' ', ' ']]

tile_topo_3 =          [['m', 'm', 'm', 'm', 'w', 'w'],
                        ['s', 's', 'f', 'm', 'w', 'w'],
                        ['s', 's', 'f', 'f', 'f', 'w']]
tile_territories_3 =   [['l', ' ', ' ', ' ', ' ', ' '],
                        ['l', 'l', ' ', ' ', ' ', ' '],
                        [' ', ' ', ' ', ' ', ' ', ' ']]

tile_topo_4 =          [['d', 'd', 'd', 'f', 'f', 'f'],
                        ['d', 'd', 'm', 'w', 'w', 'w'],
                        ['d', 'd', 'm', 'm', 'm', 'm']]
tile_territories_4 =   [[' ', ' ', ' ', ' ', ' ', 'l'],
                        [' ', ' ', ' ', ' ', ' ', 'l'],
                        [' ', ' ', ' ', ' ', ' ', ' ']]

tile_topo_5 =          [['d', 'd', 'w', 'w', 'w', 'w'],
                        ['s', 'd', 'd', 'w', 'm', 'm'],
                        ['s', 's', 's', 'm', 'm', 'm']]
tile_territories_5 =   [[' ', ' ', ' ', ' ', 'b', 'b'],
                        [' ', ' ', ' ', ' ', ' ', 'b'],
                        [' ', ' ', ' ', ' ', ' ', ' ']]

tile_topo_6 =          [['m', 'w', 'w', 'w', 'w', 'f'],
                        ['m', 'm', 's', 's', 'f', 'f'],
                        ['d', 'd', 's', 's', 's', 'f']]
tile_territories_6 =   [[' ', ' ', ' ', ' ', ' ', ' '],
                        ['b', ' ', ' ', ' ', ' ', ' '],
                        ['b', ' ', ' ', ' ', ' ', ' ']]

tiles = [(tile_topo_1, tile_territories_1),(tile_topo_2, tile_territories_2),
         (tile_topo_3, tile_territories_3),(tile_topo_4, tile_territories_4),
         (tile_topo_5, tile_territories_5),(tile_topo_6, tile_territories_6)]

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

def draw_territory(radius, orientation, color):
    start_size = t.pensize()
    start_color = t.pencolor()
    t.penup()
    t.pensize(5)
    t.pencolor(color)

    t.setheading(0)
    t.pendown()
    t.setheading(orientation)
    t.circle(radius, steps=6)
    t.setheading(0)
    t.penup()

    t.setheading(0)

    t.pensize(start_size)
    t.pencolor(start_color)

def draw_piece_territories(territories, flip):
    y_range = range(2, -1, -1) if flip else range(3)
    x_range = range(5, -1, -1) if flip else range(6)
    for i in y_range:
        for j in x_range:
            territory = tile_territory_colors.get(territories[i][j])
            if territory:
                draw_territory(hex_radius, orientation, territory)
            if flip:
                y_move = -1 if j % 2 else 1
            else:
                y_move = 1 if j % 2 else -1
            move_along_vector(1, y_move, hex_radius)
        move_along_vector(-6, 2, hex_radius)

# left to right, bottom to top
def draw_board_piece(grid_start, topos, territories, flip=False):
    move_along_vector(grid_start[0], grid_start[1], hex_radius)
    y_range = range(2, -1, -1) if flip else range(3)
    x_range = range(5, -1, -1) if flip else range(6)
    for i in y_range:
        for j in x_range:
            tile = topos[i][j]
            topo_color = tile_topo_colors[tile]
            draw_hex(hex_radius, orientation, topo_color)
            if flip:
                y_move = -1 if j % 2 else 1
            else:
                y_move = 1 if j % 2 else -1
            move_along_vector(1, y_move, hex_radius)
        move_along_vector(-6, 2, hex_radius)
    move_along_vector(0, -4, hex_radius)
    draw_piece_territories(territories, flip)
    move_along_vector(0, -4, hex_radius)


def draw_board(piece_order):
    draw_board_piece([-6,0], tiles[abs(piece_order[0])-1][0], tiles[abs(piece_order[0])-1][1], piece_order[0] < 0)
    draw_board_piece([0,-4], tiles[abs(piece_order[1])-1][0], tiles[abs(piece_order[1])-1][1], piece_order[1] < 0)
    draw_board_piece([0,-4], tiles[abs(piece_order[2])-1][0], tiles[abs(piece_order[2])-1][1], piece_order[2] < 0)
    draw_board_piece([6, 7], tiles[abs(piece_order[3])-1][0], tiles[abs(piece_order[3])-1][1], piece_order[3] < 0)
    draw_board_piece([0,-4], tiles[abs(piece_order[4])-1][0], tiles[abs(piece_order[4])-1][1], piece_order[4] < 0)
    draw_board_piece([0,-4], tiles[abs(piece_order[5])-1][0], tiles[abs(piece_order[5])-1][1], piece_order[5]< 0)



card = [1, 6, 4, 2, 5, -3]
draw_board(card)

turtle.update()
turtle.done()