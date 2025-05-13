from PIL import Image

def convert_image (fin ,fout):
    """Open the image at `fin`, convert to a RGB JPEG, and save at `fout`."""
    Image.open(fin).convert("RGB").save(fout,"JPEG")