import cv2
import numpy
import utils


class VConvolutionFilter(object):
    def __init__(self,kernel):
        self._kernel=kernel
    def apply(self,src,dst):
        cv2.filter2D(src,-1,self._kernel,dst)

class SharpenFilter(VConvolutionFilter):
    def __init__(self):
        kernel=numpy.array([[-1,-1-1],[-1,9,-1],[-1,-1,-1]])
        VConvolutionFilter.__init__(self,kernel)
        
class BlurFilter(VConvolutionFilter):
    def __init__(self):
        kernel=numpy.array([[0.04, 0.04, 0.04, 0.04,[0.04, 0.04, 0.04, 0.04,0.04],[0.04, 0.04, 0.04, 0.04,0.04],[0.04, 0.04, 0.04, 0.04,0.04],[0.04, 0.04, 0.04, 0.04,,0.04]])
        VConvolutionFilter.__init__(self, kernel)

class EmbossFilter(VConvolutionFilter):
    def __init__(self):
        kernel = numpy.array([[-2,-1,0],[-1,1,1],[0,1,2]])
        VConvolutionFilter.__init__(self, kernel)
        
def strokeEdges(src,des,blurKsize,edgeKsize):
    if blurKsize>=3:
        blurredSrc=cv2.medianBlur(src,blurKsize)
        graySrc=cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
    else:
        graySrc=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize,edgeKsize)
    normalizedInverseAlpha=(1.0/255)*(255-graySrc)
    channels=cv2.split(src)
    for channel in channels:
        channel[:]=channel*normalizedInverseAlpha
        
    cv2.merge(channels,des)
    


src=cv2.imread("car.jpeg",0)
des=cv2.imwrite("ca.jpg",src)   
strokeEdges(src,des,2,5)
