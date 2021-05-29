#!/usr/bin/env python
"""
Isman Siete, 2016

"""

from gimpfu import *
import qrcode
from qrcode.constants import *
import tempfile

temp = tempfile.NamedTemporaryFile()

correction_map = {0: ERROR_CORRECT_L,
                  1: ERROR_CORRECT_M,
                  2: ERROR_CORRECT_Q,
                  3: ERROR_CORRECT_H}


def to_PIL_color(color):
    r = int(255*color.r)
    g = int(255*color.g)
    b = int(255*color.b)
    return "rgb({0}, {1}, {2})".format(r, g, b)


def gimp_qrcode(initstr, size, border, version, correction, color, back):

    qr = qrcode.QRCode(
        version=version,
        error_correction=correction_map[correction],
        box_size=size,
        border=border,
    )
    qr.add_data(initstr)
    qr.make(fit=True)

    img_pil = qr.make_image(back_color=to_PIL_color(color), fill_color=to_PIL_color(back))
    img_pil.save(temp)

    img = pdb.file_png_load(temp.name, temp.name)
    temp.close()

    # Create a new image window
    gimp.Display(img)
    # Show the new image window
    gimp.displays_flush()


register(
    "QR_code_properties",
    "Creating a QR code using qrcode python library",
    "Creating a QR code using qrcode python library with your text string",
    "Isman Siete",
    "Isman Siete",
    "2016",
    "Create a QR code...",
    "",      # Create a new image, don't work on an existing one
    [
        (PF_STRING, "string", "Text string", "I'm a QR code!"),
        (PF_SPINNER, "size", "QR box size", 10, (1, 1000, 1)),
        (PF_SPINNER, "border", "QR border", 2, (1, 20, 1)),
        (PF_SPINNER, "version", "QR version", 1, (1, 40, 1)),
        (PF_OPTION, "correction", "Correction Level", 2, ("L", "M", "Q", "H")),
        (PF_COLOR, "color", "QR color", (0.0, 0.0, 0.0)),
        (PF_COLOR, "color", "Background color", (1.0, 1.0, 1.0))
    ],
    [],
    gimp_qrcode, menu="<Image>/File/Create")

main()
