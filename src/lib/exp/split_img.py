# write function to split image into smaller images
def split_img(img, n):
    """
    split image into n smaller images
    :param img: image to be split
    :param n: number of smaller images
    :return: list of smaller images
    """
    # get image dimensions
    w, h = img.size
    # calculate dimensions of smaller images
    w_s = int(w / n)
    h_s = int(h / n)
    # create list to store smaller images
    imgs = []
    # loop over smaller images
    for i in range(n):
        for j in range(n):
            # create smaller image
            img_s = img.crop((i * w_s, j * h_s, (i + 1) * w_s, (j + 1) * h_s))
            # add smaller image to list
            imgs.append(img_s)
    # return list of smaller images
    return imgs
# write main function
from PIL import Image
if __name__ == '__main__':

    # read image 
    img = Image.open('D:/vscode/python/101CS/assets/img/bd.jpg')
    # split image into smaller images
    imgs = split_img(img, 4)
    # loop over smaller images
    for i in range(len(imgs)):
        # save smaller image
        imgs[i].save('D:/vscode/python/101CS/assets/split/img_' + str(i) + '.jpg')