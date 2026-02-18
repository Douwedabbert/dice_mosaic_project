from PIL import Image
import numpy as np
import os


def average_gray_scale(image, num_dices_wide, num_dices_high):
    width, height = image.size
    aspect_ratio = width / height
    dice_size = width // num_dices_wide
    new_width = dice_size * num_dices_wide
    new_height = int(new_width / aspect_ratio)
    if new_height > (dice_size * num_dices_high):
        new_height = dice_size * num_dices_high
        new_width = int(new_height * aspect_ratio)

    resized_image = image.resize((new_width, new_height))

    roster = []
    for y in range(0, new_height, dice_size):
        row = []
        for x in range(0, new_width, dice_size):
            box = (x, y, x + dice_size, y + dice_size)
            square = resized_image.crop(box)
            row.append(square)
        roster.append(row)

    averages = []
    for row in roster:
        row_averages = []
        for square in row:
            gray_scale = square.convert("L").getdata()
            average = sum(gray_scale) / len(gray_scale)
            row_averages.append(average)
        averages.append(row_averages)

    return averages, dice_size, roster


def percentiles(averages, roster, twelve_dice):
    roster_percentiles = []
    min_value = min(min(arr) for arr in averages)
    max_value = max(max(arr) for arr in averages)
    total_range = max_value - min_value

    if twelve_dice:
        perc_bins = np.linspace(0, 1, 13).tolist()
    else:
        perc_bins = np.linspace(0, 1, 7).tolist()

    bins = [min_value + x * total_range for x in perc_bins]
    for row in roster:
        row_percentiles = []
        for square in row:
            gray_scale = square.convert("L").getdata()
            average = sum(gray_scale) / len(gray_scale)
            matched = False
            for k in range(len(bins) - 1):
                if (average >= bins[k] and average < bins[k + 1]) or (
                    k == len(bins) - 2 and average == bins[k + 1]
                ):
                    row_percentiles.append(k + 1)
                    matched = True
                    break
            if not matched:
                row_percentiles.append(len(bins) - 1 if average >= bins[-1] else 1)
        roster_percentiles.append(row_percentiles)

    return roster_percentiles


def load_dice_images(dice_dir, twelve_dice):
    max_index = 12 if twelve_dice else 6
    dice_images = []
    for i in range(1, max_index + 1):
        file_name = f"dice{i}.png"
        dice_image = Image.open(os.path.join(dice_dir, file_name))
        dice_images.append(dice_image)
    return dice_images


def match_dice_images(averages, dice_images, dice_size, roster_percentiles):
    width = len(averages[0]) * dice_size
    height = len(averages) * dice_size
    new_image = Image.new("RGB", (width, height))

    for y in range(len(roster_percentiles)):
        for x in range(len(roster_percentiles[y])):
            matching_dice_image = dice_images[roster_percentiles[y][x] - 1]
            matching_dice_image = matching_dice_image.resize((dice_size, dice_size))
            new_image.paste(matching_dice_image, (x * dice_size, y * dice_size))

    return new_image


def generate_dice_mosaic(file_path, max_dice, twelve_dice=True, dice_dir="Dice_imgs"):
    image = Image.open(file_path)
    width, height = image.size
    aspect_ratio = width / height
    num_dices_wide = int((max_dice * aspect_ratio) ** 0.5)
    num_dices_high = int(max_dice / num_dices_wide)

    dice_images = load_dice_images(dice_dir, twelve_dice)
    averages, dice_size, roster = average_gray_scale(image, num_dices_wide, num_dices_high)
    roster_percentiles = percentiles(averages, roster, twelve_dice)
    return match_dice_images(averages, dice_images, dice_size, roster_percentiles)
