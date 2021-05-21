import os, binascii, math, numpy as np, matplotlib.pyplot as plt

# generate grayscale image of any file
def img_gen(file):
    with open(file, 'rb') as f:

        # list to store file hexdump, line by line
        hexdump = []

        # read 16 bytes
        for chunk in iter(lambda: f.read(16), b''):
            line = binascii.hexlify(chunk).decode()
            
            # add space after every pair
            write_line = ' '.join(line[i:i+2] for i in range(0, len(line), 2))
            hexdump.append(write_line)

        hex_chars = [' ', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']

        line_num = 0

        # find number of lines
        line_count = len(hexdump)

        for line in hexdump:
            # replace all non-hex characters
            for ch in line:
                if ch not in hex_chars:
                    line = line.replace(ch, '0')

            # create matrix from first line info
            if line_num == 0:
                first_line = ''.join([char for char in line if char.isalnum()])
                dec_2d_matrix = np.zeros((line_count,int(len(first_line)/2)))

            # reoccuring variable
            line_split = line.split()

            # pad 0's if number of pairs if len of first line
            if len(line_split) < len(first_line)/2:
                line += ' 00'*int(len(first_line)/2 - len(line_split))
            
            # update reoccuring variable
            line_split = line.split()

            # fill matrix
            dec_2d_matrix[line_num] = np.fromiter((int(x, 16) for x in line_split), dtype=np.uint8)
            line_num += 1

    # generate and save image
    plt.imsave('images/' + file[:file.index(os.path.splitext(file)[1])] + '.png', dec_2d_matrix, cmap='gray')