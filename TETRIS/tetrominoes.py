from collections import namedtuple

X, O = 'X', None
Tetromino = namedtuple("Tetrimino", "name color shape")

T_long = Tetromino(name="long",
                   color="blue",
                   shape=((O,O,O,O),
                          (X,X,X,X),
                          (O,O,O,O),
                          (O,O,O,O)))

T_square = Tetromino(name="square",
                     color="yellow",
                     shape=((X,X),
                            (X,X)))

T_hat = Tetromino(name="hat",
                  color="pink",
                  shape=((O,X,O),
                         (X,X,X),
                         (O,O,O)))

T_right_snake = Tetromino(name="right_snake",
                          color="green",
                          shape=((O,X,X),
                                 (X,X,O),
                                 (O,O,O)))

T_left_snake = Tetromino(name="left_snake",
                         color="red",
                         shape=((X,X,O),
                                (O,X,X),
                                (O,O,O)))

T_left_gun = Tetromino(name="left_gun",
                       color="cyan",
                       shape=((X,O,O),
                              (X,X,X),
                              (O,O,O)))

T_right_gun = Tetromino(name="right_gun",
                        color="orange",
                        shape=((O,O,X),
                               (X,X,X),
                               (O,O,O)))

list_of_tetrominoes = [T_long, T_square, T_hat,
                       T_right_snake, T_left_snake, 
                       T_left_gun, T_right_gun]

def rotate(shape, times=1):
    """ Rotate a shape to the right """
    if times == 0:
        return shape

    rotated = [[] for _ in range(len(shape))]

    # Rotate one time to the right
    for line in shape:
        for index, atom in enumerate(line):
            rotated[index].insert(0, atom)

    return tuple(map(tuple, rotated)) if times <= 1 else rotate(rotated, times-1)

def rotate_left(shape, times=1):
    """ Rotate a shape to the left """
    return rotate(shape, 3) if times <= 1 else rotate_left(rotate(shape, 3), times-1)