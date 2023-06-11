import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import webbrowser

# Open the Tkinter file dialog window
root = tk.Tk()
root.withdraw()

# Open the file dialog for image selection
file_path = filedialog.askopenfilename()

# Read the QR codes from the selected file
if file_path:
    # Read the image
    image = cv2.imread(file_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Decode the QR codes
    qr_codes = decode(gray)

    # Loop through each QR code
    for qr_code in qr_codes:
        # Get the data of the QR code
        data = qr_code.data.decode("utf-8")
        print("QR Code Content: ", data)

        # Draw the bounding box around the QR code
        (x, y, w, h) = qr_code.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Write the content of the QR code on the image
        cv2.putText(image, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Add a "Copy Link" and "Open in Browser" button
        data_message = data + " Do you want to open it in the browser?"
        response = messagebox.askquestion("QR Code Content", data_message)
        if response == 'yes':
            webbrowser.open(data)
        else:
            # Show the results
            cv2.imshow("QR Code Reader", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
