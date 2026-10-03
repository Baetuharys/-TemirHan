import sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; sys.path.insert(0,str(ROOT))
def test_synthetic():
    try:
        import cv2, numpy as np
    except ImportError:
        print('SKIP: OpenCV/NumPy unavailable'); return
    from engines.image_to_cad.pipeline import process_image
    img=np.full((500,700),255,np.uint8)
    cv2.rectangle(img,(100,100),(600,400),0,3)
    cv2.circle(img,(250,250),35,0,3)
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'x.png'; cv2.imwrite(str(p),img)
        r=process_image(p,reference={'p1_px':[100,100],'p2_px':[600,100],'distance_mm':500},out_dir=Path(td)/'out',detection={'invert':True,'min_line_length':80})
        assert len(r['geometry']['lines'])>=4, len(r['geometry']['lines'])
        assert r['geometry']['units']=='mm'
        assert (Path(td)/'out/geometry.dxf').exists()
        assert (Path(td)/'out/geometry.json').exists()
if __name__=='__main__': test_synthetic(); print('ok: image_to_cad synthetic')
