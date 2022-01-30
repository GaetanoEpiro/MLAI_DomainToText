import numpy as np
import json
    
path = '/content/MLAI_DomainToText/data_api'

def read_images(images):
    sources = ['art_painting', 'cartoon', 'photo', 'sketch']

    for domain in sources:
        complete_path = path + '/sources/' + domain + '.txt'
    
        with open(complete_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            line = line.replace("\n", "")
            fields = line.split(" ")

            images.append(fields[0])

def select_random(number_of_samples, out_array, in_array):

    for n in range(int(number_of_samples)):
        idx = np.random.randint(0, len(in_array))

        out_array.append(in_array.pop(idx))

def write_splits_json(test, val, train):
    DatasetJson = {'test' : test, 'val' : val, 'train' : train}

    with open(path + '/data/image_splits.json', 'w') as f:
        json.dump(DatasetJson, f)

class Utils:
    def __init__(self, train=0.6, val=0.15, test=0.25):
        self.images = []
        self.validation = []
        self.training = []

        read_images(self.images)

        self.number_of_images = len(self.images)

        self.nTraining = train * self.number_of_images
        self.nValidation = val * self.number_of_images
        self.nTest = test * self.number_of_images

        np.random.shuffle(self.images)

        select_random(self.nValidation, self.validation, self.images)
        select_random(self.nTraining, self.training, self.images)

        write_splits_json(self.images, self.validation, self.training)

        print('Generated image splits')
