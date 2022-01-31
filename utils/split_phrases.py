import json
import os
import collections

path = '/content/MLAI_DomainToText/data_api/data/'

def write_dictionary(dictionary, output):
  sorted_x = sorted(dictionary.items(), reverse=True, key=lambda kv: kv[1])
  sorted_dict = collections.OrderedDict(sorted_x)

  complete_path = path + output + '_freq.txt'

  with open(complete_path, 'w') as f:
    for key in list(sorted_dict.keys()):
      f.write(str(key) + " : " + str(dictionary[key]) + '\n')

  f.close()

def insert_in_dictionary(dictionary, element):
  # Check if the word is already in dictionary
  if element in dictionary:
    # Increment count of word by 1
    dictionary[element] = dictionary[element] + 1
  else:
    # Add the word to dictionary with count 1
    dictionary[element] = 1

def split_phrases(): 
    with open(os.path.join(path, 'image_descriptions.json'), 'r') as f:
        with open(path + 'tmp.json', 'w') as f2:
            data = json.load(f)
            for img_d in data:
                for img in img_d['descriptions']:
                    texts = img.split(", ")
                    for txt in texts:
                        " ".join(txt.split())
                        f2.write(str(txt) + '\n')
    
    f.close()
    f2.close()
                
    with open(os.path.join(path, 'tmp.json'), 'r') as text:
        
        # Create an empty dictionary
        d = dict()
        phrases = dict()
            
        # Loop through each line of the file
        for line in text:
            # Remove the leading spaces and newline character
            line = line.strip()
            
            # Convert the characters in line to 
            # lowercase to avoid case mismatch
            line = line.lower()

            insert_in_dictionary(phrases, line)

            # Split the line into words
            words = line.split(" ")
            
            # Iterate over each word in line
            for word in words:
                insert_in_dictionary(d, word)
            
        # Print the contents of dictionary
        write_dictionary(d, 'word')
        write_dictionary(phrases, 'phrase')
  
    text.close()
    os.remove(os.path.join(path, 'tmp.json'))

if __name__ == '__main__':
    split_phrases()
