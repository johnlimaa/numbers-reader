import re
import PySimpleGUI as gui
import pyscreenshot as screenshot
import pytesseract as ocr
import pyperclip as clipboard


def normalizeposition(position, size):
    data = {"X": None, "Y": None, "width": None, "height": None}
    offsets = {'small': 10, 'medium': 20, 'high': 70}

    if position[0] < 0:
        data["X"] = ((position[0] * -1) + offsets['medium']) * -1
        data["width"] = (((position[0] * -1) + size[0]) - offsets['small']) * -1
    else:
        data["X"] = position[0] + offsets['medium']
        data["width"] = (position[0] + size[0]) - offsets['small']

    if position[1] < 0:
        data["Y"] = ((position[1] * -1) + offsets['high'])
        data["Y"] = (((position[1] * -1) + size[1]) + offsets['medium'])
    else:
        data["Y"] = position[1] + offsets['high']
        data["height"] = (position[1] + size[1]) + offsets['medium']

    return data


layout = [
    [gui.Button("CAPTURE"), gui.Button("COPY"), gui.Input(disabled=True, size=(480, None), key="-OUTPUT-")],
    [gui.Multiline(size=(480, 320), disabled=True)],
]

window = gui.Window("Numbers Reader", layout, size=(480, 180), resizable=True, alpha_channel=0.5)
innerWindow, capturedImg, readNumbers = None, None, None

# Use this if you have configured Tesseract in your Environment Variables
# Otherwise call it directly from it directory
# ocr.pytesseract.tesseract_cmd = "tesseract"
ocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--oem 3 --psm 6 outputbase digits'


while True:
    event, values = window.read()

    try:
        if event == "CAPTURE":
            innerWindow = normalizeposition(window.CurrentLocation(), window.Size)
            capturedImg = screenshot.grab(bbox=(innerWindow["X"],
                                                innerWindow["Y"],
                                                innerWindow["width"],
                                                innerWindow["height"]))
            readNumbers = ocr.image_to_string(capturedImg, config=custom_config)
            readNumbers = re.sub(r'\D*', '', readNumbers)
            window["-OUTPUT-"].update(readNumbers)
            clipboard.copy(readNumbers)
    except ValueError as val:
        gui.popup_error('Invalid area, try another monitor.')

    if event == "COPY":
        clipboard.copy(readNumbers)

    if event == gui.WIN_CLOSED:
        break

window.close()
