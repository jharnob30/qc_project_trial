# QC Object Detection 

*<h2>Dataset</h2>*
{Last update: 19th Mar,2024}<br/>
Dataset is collected from discord and categorized in three different category ["Measuremnet", "Packaging","Styling"] <br/>
  - Measurments -> Mostly construction .<br/>
  - Styling -> Mostly Visual and Textile.<br/>
  - Packaging -> Mostly packaging and safe -regulation related.<br/>
  - Unstructured -> Not given in category folder manner.<br/>
Although the dataset needs to be standardized and properly categorized for the betterment of model development.

<br/>
<br/>

*<h2> Yolov9 Model Training and Object detection process:</h2>* <Br/>
01. Download the ipynb file from "Object_Detection\Yolov9" <Br/>
02. Download the dataset from the same folder given used dataset (already augmented,splitted and annotated) used dataset in the initial obj detection.<Br/>
  - 2.1. Or download this "dirty_marks_detection_yolov9_71" dataset, has all the 71 dirty marks images annotated. To train one can use this dataset directly to train only.<Br/>
  - 2.2. or Download this (2.1) dataset and split in 'val' and 'train' data. For this script for splitting needed. The current code doesnt have the dataset preprocessing scripts.<Br/>
  - 2.3. Or Download visu02 folder to collect raw images from dataset directory "Dataset\Category3-Styling\VISU02" Here scopes of work is (Load, Annotate, Resize, Augment, Split, update yaml file accordingly)<Br/>
03. Upload dataset and ipynb file into google drive. <br/>
04. Run ipynb file on colab. <br/>
05. Mount drive in the script to access dataset <br/> or load dataset in the "/content" of colab and use cloud temporary storage just to play around without saving anything to drive.
06. Set {Home} directory according to your wish. Eiher you can choose "/content" for temporary colab storage or you can save everything from git clone to model in a drive by giving a directory location from drive
07. Clone git, install requirements, import libraries if needed, create weight directory and download yolov9 weights.
08. Next, if dataset needed to be preprocessed like in the point 2 said, write script here. Or load the dataset i've used in the content directory or use it from drive.
09. Before moving into the training part, yaml file needs to be updated.
  - inside this file there is defined location for test, train, validation data. so use the complete directory address for each. if the dataset has only train then use only train and remove others. or if dataset has val and train data then give the directory address of those folders. NC here means number of classes. as the dataset annotated with only one class, it is showing 1 here. "Dirty Mark"
10. After Updating ymal file, use the directory location in the training script. "#yaml file location" here. Run to train.
11. Next scripts are for validation, evaluation and test image output check. Here everytime we ecperiment or detect data or evaluate model. A new directory is created inside yolov9/runs folder. to see the output use proper folder direction. can be exp, exp2, exp3 etc as it will be given in the output cell.
12. "Inference with Custom Model" script is where we are getting to see output samples from input images. Play around it with unknow images. Remember to use proper directory adresses for model usage, input image, and output visualization.
