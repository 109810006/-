from ultralytics import YOLO
import numpy as np
import cv2

def get_model():
    model = YOLO('best.pt')
    return model

def plot_bboxes(results):
    img = results[0].orig_img 
    names = results[0].names 
    scores = results[0].boxes.conf.numpy() 
    classes = results[0].boxes.cls.numpy() 
    boxes = results[0].boxes.xyxy.numpy().astype(np.int32) 
    rgb = [[255, 0, 0],[0, 255, 0],[0, 0, 255]]
    for score, cls, bbox in zip(scores, classes, boxes):
        class_label = names[cls] 
        label = f"{class_label} : {score:0.2f}" 
        lbl_margin = 3 
        img = cv2.rectangle(img, (bbox[0], bbox[1]),
                            (bbox[2], bbox[3]),
                            color=rgb[int(cls)],
                            thickness=4)
        label_size = cv2.getTextSize(label, 
                                     fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                                     fontScale=1, thickness=1)
        lbl_w, lbl_h = label_size[0] 
        lbl_w += 2* lbl_margin
        lbl_h += 2*lbl_margin
        img = cv2.rectangle(img, (bbox[0], bbox[1]), 
                             (bbox[0]+lbl_w, bbox[1]-lbl_h),
                             color=rgb[int(cls)], 
                             thickness=-1) 
        
        cv2.putText(img, label, (bbox[0]+ lbl_margin, bbox[1]-lbl_margin), 
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=3, color=(255, 255, 255 ),
                    thickness=7)

    return img

results = get_model()('tomato.jpeg')
img = plot_bboxes(results)
'''cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
cv2.imwrite('tomato_result.jpeg', img)