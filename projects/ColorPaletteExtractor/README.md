# Color Extraction Application

## Description

The Color Extraction Application reads an image, extracts pixel data, and counts the occurrence of each color. It then
identifies the top 10 most used colors in the image. The app uses Python libraries such as `PIL` (from the `Pillow`
package) for image processing and `numpy` for handling pixel arrays.

## Requirements

Make sure to install the necessary libraries for image processing and array manipulation.

### Install requirements:

```bash
pip install pillow numpy
```

## Usage

1. **Image File Location:**

   Ensure the image file is located in the `assets` folder under the name `qr.png` or modify the file path in the code
   to match your image's location.

2. **Run the Application:**

   Execute the script to process the image and display the top 10 most used colors:

   ```bash
   python main.py
   ```

   The output will show the RGB values of the top 10 colors.

## Contributing

Feel free to create a PR if you'd like to contribute!

## License

Free to use.