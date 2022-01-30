import json
import os

path = '/content/MLAI_DomainToText/data_api/data/'

def split_phrases(): 
    img_data_dict = dict()
    with open(os.path.join(path, 'image_descriptions.json'), 'r') as f:
        with open(path + 'images_descr.json', 'w') as f2:
            data = json.load(f)
            for img_d in data:
                for img in img_d['descriptions']:
                    texts = img.split(",")
                    for txt in texts:
                        " ".join(txt.split())
                        f2.write(txt)
                        f2.write("\n")
                


    with open(os.path.join(path, 'images_descr.json'), 'r') as text:
        
        # Create an empty dictionary
        d = dict()
            
        # Loop through each line of the file
        for line in text:
            # Remove the leading spaces and newline character
            line = line.strip()
            
            # Convert the characters in line to 
            # lowercase to avoid case mismatch
            line = line.lower()
            
            # Split the line into words
            words = line.split(" ")
            
            # Iterate over each word in line
            for word in words:
                # Check if the word is already in dictionary
                if word in d:
                    # Increment count of word by 1
                    d[word] = d[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[word] = 1
            
        # Print the contents of dictionary
        import collections
        sorted_x = sorted(d.items(),reverse=True, key=lambda kv: kv[1])
        sorted_dict = collections.OrderedDict(sorted_x)
        with open(path + 'phrase_freq.txt', 'w') as f3:
            for key in list(sorted_dict.keys()):
                f3.write(key + " : " + str(d[key]))
                f3.write("\n")

if __name__ == "__main__":
    split_phrases()
