# -使用yolo v8去訓練番茄模型以及實際預測

### 使用方法
#### 前處理
建立要給模型訓練的yaml檔，提供資料集中test以及train的檔案路徑、所欲匡列的類別數量以及名稱。
```yaml
train: dataset\train 
val: dataset\test
nc: 3  # 類別數量
names: ['Initial', 'Middle', 'Harvest']
```

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
#### 評估模型指標
程式訓練完後會自動產出
- - -訓練和驗證過程它們分別對邊界框損失、分類損失和分布損失函數的變化
- - -混淆矩陣
- - -F1-Confidence Curve、Recall-Confidence Curve、Precision-Recall Curve、Precision-Confidence Curve
#### 實際預測
先將最佳的訓練權重檔案(best.pt)載入YOLO內，再使用test_tomato.py將要預測的番茄圖片輸入至模型內即可得出類別預測的結果匡列。範例 :
丟入一張具有initial、middle以及harvest類別的番茄照片:

![image](https://github.com/user-attachments/assets/67ac3857-fa66-4ed9-a0f8-a140e2b4b46c)


經過預測後之番茄結果:

![image](https://github.com/user-attachments/assets/dea919cd-86e7-40ac-a20a-f0a926dcfbb2)



