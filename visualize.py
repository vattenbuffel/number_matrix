import cv2
import numpy as np
from scipy.interpolate import interp1d
from Cell import Cell

def matrix_to_img(matrix, rows, cols, pixels_per_cell, name):
    min_color = 0
    max_color = 175
    img = np.zeros((rows*pixels_per_cell, cols*pixels_per_cell, 3), np.uint8)
    n = pixels_per_cell
    inter = interp1d([0, rows], [max_color, min_color] )

    for key in matrix:
        row, col = key
        cell:Cell = matrix[key]

        color = inter(cell.best_num_operations)
        img[row*n:(row+1)*n, col*n:(col+1)*n, 1] = color

    cv2.imwrite(name, img)

def matrices_to_surf(matrices):
    raise NotImplementedError