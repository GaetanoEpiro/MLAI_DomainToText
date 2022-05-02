# Domain-To-Text: improving Domain Generalization using Natural Language

## Authors 
* Gaetano Epiro - s277875
* Arianna Gentile - s277939
* Alessandro Lepori - s280132

## Dataset

1 - Download PACS dataset from the portal of the course in the "project_topics" folder.

2 - Place the dataset in the DomainToText_AMLProject folder making sure that the images are organized in this way:

```
PACS/kfold/art_painting/dog/pic_001.jpg
PACS/kfold/art_painting/dog/pic_002.jpg
PACS/kfold/art_painting/dog/pic_003.jpg
```

## Pretrained models

In order to reproduce the values reported in the table, you have to download the pretrained models from this link: https://drive.google.com/drive/folders/17tWDDDPY9fRLrnL3YbwkHrilq12oii2M?usp=sharing

## Environment

To run the code you have to install all the required libraries listed in the "requirements.txt" file.

For example, if you read

```
torch==1.7.0
```

you have to execute the command:

```
pip install torch==1.7.0
```

## Best checkpoint

The checkpoint containing the weights of the finetuned model with the new dataset can be downloaded from: https://drive.google.com/file/d/1wZxLYx2fWARhTAmH1tCsqbZqWDTRcZDU/view?usp=sharing