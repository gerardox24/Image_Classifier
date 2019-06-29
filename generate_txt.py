import os
import cv2

def write_txt(folder, class_number, img, object, tl, br, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img.path)
    height, width, depth = image.shape

    save_path = os.path.join(savedir, img.name.replace('jpg', 'txt'))
    temp_txt = open(save_path,'w+') 
    class_number = str(class_number)
    for obj, topl, botr in zip(object, tl, br):
        xmin = str(topl[0]/width)
        ymin = str(topl[1]/height)
        xmax = str(botr[0]/width)
        ymax = str(botr[1]/height)
        temp_txt.write('%s %s %s %s %s\n' % (class_number, xmin, ymin, xmax, ymax))
    temp_txt.close()

if __name__ == '__main__':
    ##SOLO PARA TESTING
    folder = 'images/bananas'
    img = [im for im in os.scandir(folder) if '000000' in im.name][0]
    objects = ['banana']
    tl = [(10,10)]
    br = [(100,100)]
    savedir = 'help'
    class_number = 0
    write_txt(folder, class_number, img, objects, tl, br, savedir)