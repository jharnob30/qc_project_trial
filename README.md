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
1. Download the ipynb file from "Object_Detection\Yolov9" <Br/>
2. Download the dataset from the same folder given used dataset (already augmented,splitted and annotated) used dataset in the initial obj detection.<Br/>
  - 2.1. Or download this "dirty_marks_detection_yolov9_71" dataset, has all the 71 dirty marks images annotated. To train one can use this dataset directly to train only.<Br/>
  - 2.2. or Download this (2.1) dataset and split in 'val' and 'train' data. For this script for splitting needed. The current code doesnt have the dataset preprocessing scripts.<Br/>
  - 2.3. Or Download visu02 folder to collect raw images from dataset directory "Dataset\Category3-Styling\VISU02" Here scopes of work is (Load, Annotate, Resize, Augment, Split, update yaml file accordingly)<Br/>
3. Upload dataset and ipynb file into google drive. <br/>
4. Run ipynb file on colab. <br/>
5. Mount drive in the script to access dataset <br/> or load dataset in the "/content" of colab and use cloud temporary storage just to play around with out saving anything to drive.
6. 
