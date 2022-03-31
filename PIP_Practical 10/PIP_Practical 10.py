# Aim
# Generate PDF file of your 3rd Semester Mark-sheet
#
# 20CE003_RAJ BELADIYA
# https://github.com/rajbeladiya4/PIP-Practical.git

from PIL import Image

# Path for your image where it is
image_1 = Image.open(
    r'F:\Sem 4\CE259-PIP\PIP_Practical 10\-6305456399840292285_121.JPG')

# Converting it into pdf
im_1 = image_1.convert('RGB')

# Path where your PDF file will bw saved
im_1.save(
    r'F:\Sem 4\CE259-PIP\PIP_Practical 10\Third sam marksheet.pdf')
print("File Created sucessfully at F:\Sem 4\CE259-PIP\PIP_Practical 10")
