# Object detection using Yolov2()
## Steps I follwed while doing my task
### 1)Data downloading and preprocessing
1)Downloaded the datasets(images and annotation) from the http://www.immersivelimit.com/datasets/cigarette-butts .

2)While preprocessing process I converted the anootations which are in the coco-anootations format(json) to yolo format annotations
 (xml annotatons). I wrote a script for this.
 
 3)the folder of data looks like this images:myproject/data/train/images/
                                     annotations:myproject/data/train/annottaions/
### 2)Model
For this task I used darkflow model https://github.com/thtrieu/darkflow .
#### configuring the model:
I used yolo.cfg configarations, so I eidited the configaration file accourding to my requiremnt.

I changed the number of classes (previously=80, I changed to 1) In my case its single object detection .

 I also changed the last layer filter value to 30. (filter=5(5+number of classes ))
 
### 3)Weights
I have downloaded the weights from yolo official site.

these weights are place inside a bin folder and placed in the repo.

### 4)Training
 Due to resource conflict(GPU) and Time conflict I choose only 100 images to train my model.
 
 ###### Training ststastics are listed here:
 
 training samples=100
 
 number of epochs =30
 
 learning rate=0.00001
 
 class=1
 
 backup weights= 1000
 
 optimizer=rmsprop optimizer
 
 Ckeckpoint: I created a checkpoints of weights for every 1000 smples and can be found in ckpt file.We can load our model from next time from that checkpoint.
 
 
 note:The accuracy of the model as for as now is too low because i trained only 100 samples to check whether training is possible .
 
#### files :
##### 1)convert_json_to_xml:python file which reads json annotations of cigg_butts datasets  and converts to yolo xml format.
##### 2) gnani.py : python file for training the model

Note: train test and validtation has to be done .
