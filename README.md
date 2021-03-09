<h2 align="center">
Reading numbers
</h2>

<p align="center">
  <img href Alt="Language" src="https://img.shields.io/badge/language-Python-lightgrey">
  <img href Alt="Creator" src="https://img.shields.io/badge/by-John%20Lima-blue">
</p>

### About
This application is used to read the numbers instead of the barcode on a bill, using OCR, and copy it to user's clipboard.
I tried to use third party barcodes, but they were inaccurate in my tests. So I took the advice of a friend and created this tool.
It's functional on Windows and I'm working on a Linux version.

### What are its dependencies? 
* PySimpleGUI
* pytesseract
* pyscreenshot
* pyperclip
* Tesseract OCR

> When you run this script, it automatically installs its dependencies.

### Installing Tesseract
I used an Open Source called Tesseract, to install it you follow the instructions on this <a href="https://github.com/UB-Mannheim/tesseract/wiki">website</a>.

### Running
If you have installed all dependencies globally, a simple double click should execute this application.<br>
Otherwise, if you installed from a virtual envioriment (virtualenv). You'll need to run it at the prompt command.<br>

### Application
<p align="center">
  <img src="https://user-images.githubusercontent.com/47035885/110405442-633b2100-805f-11eb-80d1-6ef3a274ae79.png" width="500px" />
</p> 
When running, you can resize the app to fit the length of the number in bill.
<br>
<p align="center">
  <img src="https://user-images.githubusercontent.com/47035885/110404225-3e45ae80-805d-11eb-9f57-e3652e31138e.jpeg" width="500px" />
</p>
It will ignore all caracters except numbers. In this image, you can see the result when it succefully read a number. Automatically you'll have the number read on your clipboard. Try to paste it.
