import tkinter as t
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    qr_data = entry.get()
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((200, 200), Image.NEAREST)# Use Image.NEAREST for no antialiasing
    img_t = ImageTk.PhotoImage(img)
    qr_label.config(image=img_t)
    qr_label.image = img_t

# Create the main window
root = t.Tk()
root.title("QR Code Generator")

# Create a label for the input
entry_label = t.Label(root, text="Enter data for QR code:")
entry_label.pack()

# Create an entry field for the user input
entry = t.Entry(root, width=30)
entry.pack()

# Create a button to generate the QR code
generate_button = t.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack()

# Create a label to display the generated QR code
qr_label = t.Label(root)
qr_label.pack()

root.mainloop()