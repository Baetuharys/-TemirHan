def preprocess(path, threshold=None, invert=False):
    try:
        import cv2
    except ImportError as e:
        raise RuntimeError('OpenCV is required for raster preprocessing; install requirements.txt') from e
    img=cv2.imread(str(path),cv2.IMREAD_GRAYSCALE)
    if img is None: raise FileNotFoundError(path)
    img=cv2.GaussianBlur(img,(3,3),0)
    if threshold is None:
        _,bw=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    else:
        _,bw=cv2.threshold(img,int(threshold),255,cv2.THRESH_BINARY)
    if invert: bw=cv2.bitwise_not(bw)
    edges=cv2.Canny(bw,50,150,apertureSize=3)
    return {'gray':img,'binary':bw,'edges':edges}
