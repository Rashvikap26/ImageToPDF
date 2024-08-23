

# ImgToPdf

ImgToPdf is a simple Tkinter-based application that converts selected images into a PDF file. The application allows users to select multiple images, specify the output PDF file name, and convert the images into a neatly formatted PDF.

## Features

- Select multiple images for conversion.
- Preview selected image names in a list.
- Specify a custom name for the output PDF.
- Automatically scale and center images in the PDF.

## Requirements

- Python 
- Tkinter
- ReportLab
- Pillow

## Installation

Install Dependencies:

   Install the required Python packages using pip. It’s recommended to use a virtual environment.

   ...
   pip install reportlab pillow
   ...

   Note: Tkinter is included with most Python installations, but if you encounter issues, you may need to install it separately depending on your operating system.

Usage

Run the Application:

   ```
   python img_to_pdf.py
   ```
Select Images:
   - Click on the **Select** button to open a file dialog.
   - Choose the images you want to convert (supports `.png`, `.jpg`, and `.jpeg` formats).
Enter PDF Name:
   - Type the desired name for the output PDF in the provided text entry field.

Convert to PDF:
   - Click on the **Convert to PDF** button to generate the PDF.
   - The output PDF will be saved in the same directory with the name specified in the text entry field, or as `output.pdf` if no name is provided.

## Example

1. Run the application:

   ```bash
   python img_to_pdf.py
   ```

2. Select images from your file system.

3. Enter `my_document` as the PDF name.

4. Click **Convert to PDF**.

   - A file named `my_document.pdf` will be created in the application’s directory, containing the selected images.

## Code Overview

- **`img_to_pdf.py`**: Contains the main code for the ImgToPdf application.
  - `ImgToPdf` class: Handles the application logic and user interface.
  - Methods:
    - `initialize_ui()`: Sets up the UI components.
    - `select_imgs()`: Opens a file dialog to select images.
    - `update_selected_img_list()`: Updates the listbox with selected image names.
    - `convert_img_to_pdf()`: Converts the selected images into a PDF.

## Troubleshooting

- **Tkinter Not Found**: Ensure Tkinter is installed. On some systems, it may require a separate installation.
- **Library Import Issues**: Make sure all required libraries (`reportlab`, `pillow`) are installed in your Python environment.

