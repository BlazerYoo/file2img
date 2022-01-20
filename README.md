# file2img

Complete pipeline for generating images for any file used for malware machine learning research

Run `git clone https://github.com/BlazerYoo/file2img.git` or [download](https://github.com/BlazerYoo/file2img/archive/refs/heads/main.zip) repo.

Run `pip install -r requirements.txt` to install dependencies.

`imgen_color.py` generates color image of any file with dimensions corresponding to file size

`imgen_color_resize.py` generates color image of any file with uniform square dimensions

`imgen_gray.py` generates grayscale image of any file with dimensions corresponding to file size

`imgen_gray_resize.py` generates grayscale image of any file with uniform square dimensions

## Usage

```
usage: python run.py [--help] [--file FILE_PATH] []

Generate images of any file

arguments:
    --help, -h           : display this help menu and exit
    --file, -f FILE_PATH : path of file to send to generate image of
    --style, -s STYLE    : style of image to generate in
                           (color, color_resize, gray, gray_resize)

example:
python run.py ffmpeg.exe
```

## Example

|Resize color image of `ffmpeg.exe`|Resized grayscale image of `ffmpeg.exe`|
| ----------- | ----------- |
|![image](https://user-images.githubusercontent.com/69565038/150297529-20d1b242-db6f-4b98-9444-7b403ec281a7.png)|![image](https://user-images.githubusercontent.com/69565038/150297608-8765c106-7942-4e39-ba64-7a7d72639c9f.png)|

## License

Read the [AGPL-3.0 License](https://github.com/BlazerYoo/file2img/blob/main/LICENSE)
