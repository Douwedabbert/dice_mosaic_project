import os
import numpy as np
import cv2


def add_circle(img, pos_x, pos_y, value, eyes_diameter):
    radius = eyes_diameter // 2
    cv2.circle(img, (pos_x, pos_y), radius, (value, value, value), -1)


def create_dice_images(output_dir, size=200, eyes_diameter=60, verbose=True):
    width = size
    height = size
    center = round(width / 2)
    outside = 34

    empty_img = np.ones((width, height), dtype=np.uint8)

    empty_img.fill(255)
    white1 = np.copy(empty_img)
    add_circle(white1, center, center, 0, eyes_diameter)
    if verbose:
        print("drawing white 1 done")

    white2 = np.copy(empty_img)
    add_circle(white2, outside, outside, 0, eyes_diameter)
    add_circle(white2, width - outside, width - outside, 0, eyes_diameter)
    if verbose:
        print("drawing white 2 done")

    white3 = np.copy(white2)
    add_circle(white3, center, center, 0, eyes_diameter)
    if verbose:
        print("drawing white 3 done")

    white4 = np.copy(white2)
    add_circle(white4, width - outside, outside, 0, eyes_diameter)
    add_circle(white4, outside, width - outside, 0, eyes_diameter)
    if verbose:
        print("drawing white 4 done")

    white5 = np.copy(white4)
    add_circle(white5, center, center, 0, eyes_diameter)
    if verbose:
        print("drawing white 5 done")

    white6 = np.copy(white4)
    add_circle(white6, outside, center, 0, eyes_diameter)
    add_circle(white6, width - outside, center, 0, eyes_diameter)
    if verbose:
        print("drawing white 6 done")

    empty_img.fill(0)
    black1 = np.copy(empty_img)
    add_circle(black1, center, center, 255, eyes_diameter)
    if verbose:
        print("drawing black 1 done")

    black2 = np.copy(empty_img)
    add_circle(black2, outside, outside, 255, eyes_diameter)
    add_circle(black2, width - outside, width - outside, 255, eyes_diameter)
    if verbose:
        print("drawing black 2 done")

    black3 = np.copy(black2)
    add_circle(black3, center, center, 255, eyes_diameter)
    if verbose:
        print("drawing black 3 done")

    black4 = np.copy(black2)
    add_circle(black4, width - outside, outside, 255, eyes_diameter)
    add_circle(black4, outside, width - outside, 255, eyes_diameter)
    if verbose:
        print("drawing black 4 done")

    black5 = np.copy(black4)
    add_circle(black5, center, center, 255, eyes_diameter)
    if verbose:
        print("drawing black 5 done")

    black6 = np.copy(black4)
    add_circle(black6, outside, center, 255, eyes_diameter)
    add_circle(black6, width - outside, center, 255, eyes_diameter)
    if verbose:
        print("drawing black 6 done")

    os.makedirs(output_dir, exist_ok=True)

    cv2.imwrite(os.path.join(output_dir, "dice1.png"), black1)
    cv2.imwrite(os.path.join(output_dir, "dice2.png"), black2)
    cv2.imwrite(os.path.join(output_dir, "dice3.png"), black3)
    cv2.imwrite(os.path.join(output_dir, "dice4.png"), black4)
    cv2.imwrite(os.path.join(output_dir, "dice5.png"), black5)
    cv2.imwrite(os.path.join(output_dir, "dice6.png"), black6)

    cv2.imwrite(os.path.join(output_dir, "dice7.png"), white1)
    cv2.imwrite(os.path.join(output_dir, "dice8.png"), white2)
    cv2.imwrite(os.path.join(output_dir, "dice9.png"), white3)
    cv2.imwrite(os.path.join(output_dir, "dice10.png"), white4)
    cv2.imwrite(os.path.join(output_dir, "dice11.png"), white5)
    cv2.imwrite(os.path.join(output_dir, "dice12.png"), white6)
