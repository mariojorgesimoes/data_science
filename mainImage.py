import matplotlib.image as mpimg
from matplotlib import pyplot as plt

img = mpimg.imread('image008.jpg')


# plt.axis('off')
# plt.imshow(img)

# print(img)

def realcarVermelho(imagem, fator):
    imagem[:, :, 2] = imagem[:, :, 2] * fator
    plt.figure(imagem[:, :, 2])
    imagem_realcada = imagem[:, :, 2]
    return imagem_realcada


print(realcarVermelho(img, 2))

# def efeitoMosaico(imagem, W):
#   for i in range(1,len())
