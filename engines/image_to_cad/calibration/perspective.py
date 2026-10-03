def rectify(image, src_points, output_size):
    """Rectify a planar quadrilateral. src_points: TL,TR,BR,BL pixels; output_size=(w,h)."""
    try:
        import cv2, numpy as np
    except ImportError as e:
        raise RuntimeError('OpenCV and NumPy required') from e
    if len(src_points)!=4: raise ValueError('four source points required')
    w,h=map(int,output_size)
    src=np.array(src_points,dtype='float32')
    dst=np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]],dtype='float32')
    M=cv2.getPerspectiveTransform(src,dst)
    return cv2.warpPerspective(image,M,(w,h)),M
