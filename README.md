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
  model.train(data="train.yaml", epochs=30, batch=10, lr0=0.001 )
```
#### 評估模型
程式訓練完後會自動產出訓練和驗證過程它們分別對邊界框損失、分類損失和分布損失函數的變化。也會產出recall、AP值以及mAP。如下圖:
![image](https://github.com/user-attachments/assets/caef1b57-a908-4609-997e-f8f4ac6276c5)
亦會產生混淆矩陣來評估模型對於各類別的辨識能力，如下圖:
![image](https://github.com/user-attachments/assets/e23873e7-ff26-452c-b53f-de15e00c4e28)
#### 實際預測
先將最佳的訓練權重檔案(best.pt)載入YOLO內，再將要預測的番茄圖片輸入至模型內即可得出類別預測的結果匡列。範例 :
丟入一張具有initial、middle以及harvest類別的番茄照片:

![image](https://github.com/user-attachments/assets/67ac3857-fa66-4ed9-a0f8-a140e2b4b46c)


經過預測後之番茄結果:

![image](https://github.com/user-attachments/assets/dea919cd-86e7-40ac-a20a-f0a926dcfbb2)



