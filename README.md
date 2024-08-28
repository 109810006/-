# -使用yolo v8去訓練番茄模型

### 使用方法
#### 前處理



#### 訓練
先載入yolo套件 ```from ultralytics import YOLO ```
再將以經過預訓練的權重載入模型內，最後使用model.train並設置欲訓練參數。
目前設置 
epochs=30, batch=10,lr0=0.001

``` python
from ultralytics import YOLO
if __name__ == '__main__':
  model = YOLO("yolov8n.pt")
  model.train(data="train.yaml", epochs=30, batch=10,lr0=0.001)
```
#### 評估模型





#### 預測
先將最佳的訓練權重檔案(best.pt)載入YOLO內，再將要預測的番茄圖片輸入至模型內即可得出類別預測的結果。


### 目前成果
![image](https://github.com/user-attachments/assets/92c7892c-ab15-466d-8e8c-1adcb2eec12b)

