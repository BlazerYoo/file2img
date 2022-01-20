from imgen_color import img_gen as color
from imgen_color_resize import img_gen as color_resize
from imgen_gray import img_gen as gray
from imgen_gray_resize import img_gen as gray_resize

import sys

def argSearch(shortFlag, longFlag):
    for index in range(len(sys.argv)):
        if sys.argv[index].lower() == shortFlag or sys.argv[index].lower() == longFlag:
            try:
                return True, sys.argv[index+1]
            except:
                print('No argument after', sys.argv[index], 'flag.')
                return False, None
    return False, None

# Help menu
for arg in sys.argv:
    if arg.lower() == '-h' or arg.lower() == '--help':
        print('''
usage: python run.py [--help] [--file FILE_PATH] []

Scan your file across multiple antivirus engines

arguments:
    --help, -h           : display this help menu and exit
    --file, -f FILE_PATH : path of file to send to generate image of
    --style, -s STYLE    : style of image to generate in
                           (color, color_resize, gray, gray_resize)

example:
python run.py chrome.exe''')

    else:
        # File and style
        (fileFound, file) = argSearch('-f', '--file')
        (styleFound, style) = argSearch('-s', '--style')

        if fileFound:
            if styleFound:
                if style.lower() == 'color':
                    color(file)
                elif style.lower() == 'color_resize':
                    color_resize(file)
                elif style.lower() == 'gray':
                    gray(file)
                elif style.lower() == 'gray_resize':
                    gray_resize(file)
                else:
                    print('Style not available. Choose one of color, color_resize, gray, gray_resize.')