# QR Code Scanner

This is a Python script that allows you to scan QR codes from an image.

## Requirements

- Python 3.x
- OpenCV
- pyzbar

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/TitanHaxz/QR-Code-Scanner.git
   ```

2. Install the required dependencies:
  ```bash
  pip install opencv-python pyzbar
  ```

## Usage

1. Run the script:
  ```bash
  python main.py
  ```

2. A file dialog window will open, allowing you to select an image containing QR codes.

3. The script will detect the QR codes in the image and display their contents.

4. If the QR code content is a URL, you will be prompted to open it in a web browser.

## License

This project is licensed under the [MIT License](./LICENSE).

