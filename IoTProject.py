!pip install pytesseract
!pip install google-colab
!apt install tesseract-ocr


import io
from PIL import Image
import pytesseract
from google.colab import files

# Upload the image file
uploaded = files.upload()

# Specify the path to the image you want to perform OCR on
image_path_in_colab = next(iter(uploaded))

# Read the image using PIL
image = Image.open(io.BytesIO(uploaded[image_path_in_colab]))

# Perform OCR
extracted_information = pytesseract.image_to_string(image)

# Function to search for a word in the extracted text and highlight it
def search_and_highlight(target_word, extracted_text):
    word_count = 0
    highlighted_text = extracted_text.replace(target_word, '\033[1m{}\033[0m'.format(target_word))
    word_count = highlighted_text.count('\033[1m{}\033[0m'.format(target_word))
    return word_count, highlighted_text

# The target word to search for
target_word = input("Enter the word you want to target: ")

# Search for the target word in the extracted text and highlight it
word_count, highlighted_text = search_and_highlight(target_word, extracted_information)

# Display the highlighted text
print(highlighted_text)

print("Occurrences of '{}' in the extracted text: {}".format(target_word, word_count))
