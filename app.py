import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os

class ImgToPdf:
    def __init__(self, root):
        self.root = root
        self.img_paths = []  # List to store image paths
        self.pdf_name = tk.StringVar()  # Variable to store PDF name
        self.initialize_ui()  # Initialize UI

    def initialize_ui(self):
        # Create the UI components
        title_label = tk.Label(self.root, text="Image to PDF", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        select_img_button = tk.Button(self.root, text="Select", command=self.select_imgs)
        select_img_button.pack(pady=(0, 10))
        
        # Add Listbox for image selection
        self.select_img_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.select_img_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        label = tk.Label(self.root, text="Enter output PDF name:")
        label.pack()

        # Entry to store the name
        self.pdf_name_entry = tk.Entry(self.root, textvariable=self.pdf_name, width=40, justify="center")
        self.pdf_name_entry.pack()

        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_img_to_pdf)
        convert_button.pack(pady=(20, 40))

    def select_imgs(self):
        self.img_paths = filedialog.askopenfilenames(
            title="Select images",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        self.update_selected_img_list()

    def update_selected_img_list(self):
        self.select_img_listbox.delete(0, tk.END)
        for img_path in self.img_paths:
            _, img_name = os.path.split(img_path)
            self.select_img_listbox.insert(tk.END, img_name)

    def convert_img_to_pdf(self):
        if not self.img_paths:
            return
        
        output_pdf_path = self.pdf_name.get() + ".pdf" if self.pdf_name.get() else "output.pdf"

        pdf = canvas.Canvas(output_pdf_path, pagesize=(612, 792))

        for img_path in self.img_paths:
            img = Image.open(img_path)
            available_width = 540
            available_height = 720
            scale_factor = min(available_width / img.width, available_height / img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor
            x_centered = (612 - new_width) / 2
            y_centered = (792 - new_height) / 2

            pdf.setFillColorRGB(255, 255, 255)
            pdf.rect(0, 0, 612, 792, fill=True)
            pdf.drawInlineImage(img_path, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()

        pdf.save()

def main():
    root = tk.Tk()
    root.title("Img To PDF")
    root.geometry("500x700")
    app = ImgToPdf(root)
    root.mainloop()

if __name__ == "__main__":
    main()
