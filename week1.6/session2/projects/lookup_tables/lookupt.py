class Img():
    def __init__(self, width, height, value=0, maximum=255, url=""):
        self.width = width
        self.height = height
        self.value = value
        self.max = maximum
        self.url = url

    def readPGM(self):

        with open(self.url,"r") as f:    # read in the file
            data = f.readlines()
            
        data = [line.strip().split() for line in data[1:]] # clean the space-separated data, skip the first line
            
        width = int(data[0][0]) # store the data - compare to the text in the file
        height = int(data[0][1])
        max_gray = int(data[1][0])
        pixels = [[int(data[2+i][j]) for j in range(width)] for i in range(height)] # nested list comprehension for pixel array
        
        return width,height,max_gray,pixels   # tuple of PGM data


class Lut():
    def __init__(self, pgmfile):
        self.file = pgmfile

    def apply(self):
