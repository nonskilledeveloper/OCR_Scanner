# OCR_Scanner

This is a simple script written in Python to extract phone numbers and usernames from a set of images using OCR. The extracted data is saved in a CSV file named contacts.csv.

To use this script, you will need to have Python installed on your machine. You will also need to install the following packages:

* pytesseract
* PIL
* csv

You can install these packages using pip by running the following command:

`pip install pytesseract Pillow csv`

You will also need to install Tesseract OCR on your machine. You can download the installer for Tesseract OCR from the following link:
https://github.com/UB-Mannheim/tesseract/wiki

Once you have installed the required packages and Tesseract OCR, you can run the script by executing the following command:

`python contact_parser.py`

# Usage

To use this script, you will need to capture images containing phone numbers and usernames. The images should be named as follows:

`1.png, 2.png, 3.png, ...`

You can also use JPEG images, but you will need to change the file extension in the script.

The script will extract phone numbers and usernames from each image and save the data in a CSV file named contacts.csv.

# Notes

* This script is only designed to extract phone numbers with 10 digits.
* Usernames are identified by the "@" symbol at the beginning of the text.
* Usernames must be between 7 and 25 characters long.
* The script will discard any phone numbers or usernames that contain invalid characters.
* If there are more phone numbers than usernames in a single image, or vice versa, the script will print a warning message.

# License

This project is licensed under the GNU General Public License v3.0 - see the [<u>LICENSE</u>](https://github.com/nonskilledeveloper/OCR_Scanner/blob/main/LICENSE) file for details.

# Acknowledgments
Thanks to the developers of pytesseract, PIL, and csv for creating these helpful packages.
