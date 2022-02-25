# remove text from image
from PIL import Image
def rmv_txt(img):
    """
    remove text from image
    :param img: image to be processed
    :return: image without text
    """
    # convert image to grayscale
    img = img.convert('L')
    # get image dimensions
    w, h = img.size
    # create list to store pixels
    pxl = []
    # loop over image pixels
    for i in range(w):
        for j in range(h):
            # get pixel value
            pxl.append(img.getpixel((i, j)))
    # create list to store pixels
    pxl_new = []
    # loop over pixels
    for i in range(len(pxl)):
        # if pixel value is greater than 200
        if pxl[i] > 200:
            # append pixel to list
            pxl_new.append(pxl[i])
        # else
        else:
            # append 0 to list
            pxl_new.append(0)
   # return image without text
    return Image.fromarray(pxl_new).convert('L')
# main function
if __name__ == '__main__':
    # read image 
    img = Image.open('D:/vscode/python/101CS/assets/img/woman.jpg')
    # remove text from image
    img_rmv = rmv_txt(img)
    # save image
    img_rmv.save('D:/vscode/python/101CS/assets/img/woman_rmv.jpg')