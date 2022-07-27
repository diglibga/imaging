import os, re
from PIL import Image

path = input('What directory would you like to run this on? ')
# Change to path directory
os.chdir(path)

# Specify Max thumbnail size
MAX_SIZE = (300, 300)

# Find files for conversion
imgfiles = [fi for fi in os.listdir(path) if fi.endswith((".png", ".jpg", ".jp2"))]
pdffiles = [fi for fi in os.listdir(path) if fi.endswith('.pdf')]

if imgfiles is not None:
    # Do work on image files
    for f in imgfiles:
        # Do modifications for filename
        imgfile_rpl1 = os.path.splitext(f)[0] + ".jpg"
        imgfile_rpl2 = imgfile_rpl1.replace("full_", "")
        imgfile_rpl3 = re.sub('-\d\d\d\d\d\d', r'', imgfile_rpl2)
        imgfile_name = re.sub('-\d\d\d\d\d', r'', imgfile_rpl3)
        print("Converting ", imgfile_name)

        # Open image and create thumbnail
        image = Image.open(f)
        image.thumbnail(MAX_SIZE)
        image.save(imgfile_name, "JPEG")
