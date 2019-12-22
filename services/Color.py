import math

def next_color(c_from, c_to, d_r_col, d_g_col, d_b_col):
    c_r = c_from[0] - d_r_col if c_from[0] > c_to[0] else c_from[0] + d_r_col
    c_g = c_from[1] - d_g_col if c_from[1] > c_to[1] else c_from[1] + d_g_col
    c_b = c_from[2] - d_b_col if c_from[2] > c_to[2] else c_from[2] + d_b_col

    return (c_r, c_g, c_b)

def get_delta_color(c_from, c_to, step):
    d_r_col = math.floor(c_from[0] - c_to[0]) if c_from[0] > c_to[0] else math.floor(c_to[0] - c_from[0])
    d_r_col = math.floor(d_r_col / step) if d_r_col != 0 else 0
    d_g_col = math.floor(c_from[1] - c_to[1]) if c_from[1] > c_to[1] else math.floor(c_to[1] - c_from[1])
    d_g_col = math.floor(d_g_col / step) if d_g_col != 0 else 0
    d_b_col = math.floor(c_from[2] - c_to[2]) if c_from[2] > c_to[2] else math.floor(c_to[2] - c_from[2])
    d_b_col = math.floor(d_b_col / step) if d_b_col != 0 else 0

    return (d_r_col, d_g_col, d_b_col)

def get_color(c_from, c_to, step):
    delta_color = get_delta_color(c_from, c_to, step)
    previous_color = next_color(c_from, c_to, delta_color[0], delta_color[1], delta_color[2])
    while True:
        previous_color = next_color(previous_color, c_to, delta_color[0], delta_color[1], delta_color[2])
        yield previous_color