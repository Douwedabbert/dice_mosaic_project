import os

from Generate_dice import create_dice_images
from dice_mosaic import generate_dice_mosaic


# Central configuration
FILE_PATH = "Test.JPEG" # Choose image to turn into mosaic
MAX_DICE = 10000 # Choose max number of dice to be used for mosaic
TWELVE_DICE = True
DICE_OUTPUT_DIR = "Dice_imgs"
MOSAIC_OUTPUT_PATH = "dice_mosaic_output.png"
REGENERATE_DICE_IMAGES = True
SHOW_PREVIEW = True


def main():
    if REGENERATE_DICE_IMAGES:
        create_dice_images(output_dir=DICE_OUTPUT_DIR)

    new_image = generate_dice_mosaic(
        file_path=FILE_PATH,
        max_dice=MAX_DICE,
        twelve_dice=TWELVE_DICE,
        dice_dir=DICE_OUTPUT_DIR,
    )

    output_dir = os.path.dirname(MOSAIC_OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    new_image.save(MOSAIC_OUTPUT_PATH)
    print(f"Saved mosaic to: {MOSAIC_OUTPUT_PATH}")

    if SHOW_PREVIEW:
        new_image.show()


if __name__ == "__main__":
    main()
