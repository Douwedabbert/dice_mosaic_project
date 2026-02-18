# Dice Mosaic Generator

This project converts an input image into a mosaic made of dice face images.

## Files

- `main.py`: Single entry point and all runtime configuration.
- `dice_mosaic.py`: Image-to-dice matching and mosaic generation logic.
- `Generate_dice.py`: Utility for generating the `dice1.png` to `dice12.png` assets.
- `Dice_imgs/`: Dice face images used to build the mosaic.

## How It Works

1. The input image is resized to a dice grid.
2. Each grid cell is converted to grayscale and averaged.
3. Each average value is mapped to a die face bucket.
4. The matching die image is pasted into the output canvas.

## Setup

1. Install dependencies:
   - `Pillow`
   - `numpy`
   - `opencv-python`

Example:

```bash
pip install pillow numpy opencv-python
```

## Run

Edit settings in `main.py`:

- `FILE_PATH`: input image path
- `MAX_DICE`: approximate maximum number of dice in the mosaic
- `TWELVE_DICE`: `True` for 12 dice variants, `False` for 6
- `DICE_OUTPUT_DIR`: folder containing dice images
- `MOSAIC_OUTPUT_PATH`: output image path
- `REGENERATE_DICE_IMAGES`: regenerate dice assets before mosaic generation
- `SHOW_PREVIEW`: display the output image after saving

Then run:

```bash
python3 main.py
```

## Notes

- If `REGENERATE_DICE_IMAGES = True`, new dice images are written to `DICE_OUTPUT_DIR`.
- Output is always saved to `MOSAIC_OUTPUT_PATH`.
