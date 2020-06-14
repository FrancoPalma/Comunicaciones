from skimage import io, color, feature
from skimage.filters import rank
rgbImg = io.imread(imgFlNm)
grayImg = color.rgb2gray(rgbImg)
print(grayImg.shape) # (667,1000), a 2 dimensional grayscale image

glcm = feature.greycomatrix(grayImg, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
print(glcm.shape) # (256, 256, 1, 4)

rank.entropy(glcm, disk(5)) # throws an error since entropy expects a 2-D array in its arguments

rank.entropy(grayImg, disk(5)) # given an output. 
