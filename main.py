import re
import PySimpleGUI as gui
import pyscreenshot as screenshot
import pytesseract as ocr
import pyperclip as clipboard


def normalizeposition(position, size):
    data = {"X": None, "Y": None, "width": None, "height": None}

    if position[0] < 0:
        data["X"] = ((position[0] * -1) + 20) * -1
        data["width"] = (((position[0] * -1) + size[0]) - 10) * -1
    else:
        data["X"] = position[0] + 20
        data["width"] = (position[0] + size[0]) - 10

    if position[1] < 0:
        data["Y"] = ((position[1] * -1) + 70)
        data["Y"] = (((position[1] * -1) + size[1]) + 20)
    else:
        data["Y"] = position[1] + 70
        data["height"] = (position[1] + size[1]) + 20

    return data


layout = [
    [gui.Button("CAPTURE"), gui.Button("COPY"), gui.Input(disabled=True, size=(480, None), key="-OUTPUT-")],
    [gui.Multiline(size=(480, 320), disabled=True)],
]

window = gui.Window("Numbers Reader", layout, size=(480, 180), resizable=True, alpha_channel=0.5)
innerWindow, capturedImg, readNumbers = None, None, None

# Use this if you have configured Tesseract in your Environment Variables
# Otherwise call it directly from it directory
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ocr.pytesseract.tesseract_cmd = "tesseract"
custom_config = r'--oem 3 --psm 6 outputbase digits'


while True:
    event, values = window.read()

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

    if event == "COPY":
        clipboard.copy(readNumbers)

    if event == gui.WIN_CLOSED:
        break

window.close()
