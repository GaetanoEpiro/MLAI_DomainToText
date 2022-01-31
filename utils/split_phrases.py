import json
import os
import collections

path = '/content/MLAI_DomainToText/data_api/data/'

def write_dictionary(dictionary, output, out_file_name):
  sorted_x = sorted(dictionary.items(), reverse=True, key=lambda kv: kv[1])
  sorted_dict = collections.OrderedDict(sorted_x)

  complete_path = path + output + '_freq' + out_file_name + '.txt'

  with open(complete_path, 'w') as f:
    for key in list(sorted_dict.keys()):
      f.write(str(key) + " : " + str(dictionary[key]) + '\n')

def insert_in_dictionary(dictionary, element):
  # Check if the word is already in dictionary
  if element in dictionary:
    # Increment count of word by 1
    dictionary[element] = dictionary[element] + 1
  else:
    # Add the word to dictionary with count 1
    dictionary[element] = 1

def read_splits(train_images):
  with open(os.path.join(path, 'image_splits.json'), 'r') as f:
    data = json.load(f)

    for image in data['train']:
      train_images.append(image)    

def generate_dictionary(output, words_dict, phrases_dict, out_file_name):
    with open(os.path.join(path, output), 'r') as text:
        # Loop through each line of the file
        for line in text:
            # Remove the leading spaces and newline character
            line = line.strip()
            
            # Convert the characters in line to 
            # lowercase to avoid case mismatch
            line = line.lower()

            insert_in_dictionary(phrases_dict, line)

            # Split the line into words
            words = line.split(" ")
            
            # Iterate over each word in line
            for word in words:
                insert_in_dictionary(words_dict, word)
            
        # Print the contents of dictionary
        write_dictionary(words_dict, 'word', out_file_name)
        write_dictionary(phrases_dict, 'phrase', out_file_name)

def split_phrases(): 
    train_images = []  

    read_splits(train_images)
    
    with open(os.path.join(path, 'image_descriptions.json'), 'r') as f:
        with open(path + 'tmp.json', 'w') as f2:
            with open(path + 'tmp_train.json', 'w') as train_f:
              data = json.load(f)
              for img_d in data:
                  for img in img_d['descriptions']:
                      texts = img.split(", ")
                      for txt in texts:
                          " ".join(txt.split())
                          f2.write(str(txt) + '\n')

                  if img_d['image_name'] in train_images:
                    for img in img_d['descriptions']:
                      texts = img.split(", ")
                      for txt in texts:
                        " ".join(txt.split())
                        train_f.write(str(txt) + '\n')
                
    # Create an empty dictionary
    words_train_dict = dict()
    phrases_train_dict = dict()
    words_dict = dict()
    phrases_dict = dict()

    generate_dictionary('tmp.json', words_dict, phrases_dict, '')
    generate_dictionary('tmp_train.json', words_train_dict, phrases_train_dict, '_train')

    os.remove(os.path.join(path, 'tmp.json'))
    os.remove(os.path.join(path, 'tmp_train.json'))


if __name__ == '__main__':
    split_phrases()
