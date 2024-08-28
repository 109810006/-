from ultralytics import YOLO
if __name__ == '__main__':
  model = YOLO("yolov8n.pt")
  model.train(data="train.yaml", epochs=30, batch=10,lr0=0.001)
