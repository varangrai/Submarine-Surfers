import numpy as np


def sceneRadianceRGB(img, transmission, AtomsphericLight):
    sceneRadiance = np.zeros(img.shape)
    img = np.float16(img)
    for i in range(0, 3):
        sceneRadiance[:, :, i] = (img[:, :, i] - AtomsphericLight[i]) / transmission[:, :, i]  + AtomsphericLight[i]
       
        for j in range(0, sceneRadiance.shape[0]):
            for k in range(0, sceneRadiance.shape[1]):
                if sceneRadiance[j, k, i] > 255:
                    sceneRadiance[j, k, i] = 255
                if sceneRadiance[j, k, i] < 0:
                    sceneRadiance[j, k, i] = 0
    sceneRadiance = np.uint8(sceneRadiance)

    return sceneRadiance


