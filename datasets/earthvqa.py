# EarthVQA dataset class that handles loading and formatting the EarthVQA specific JSON data
# For a different type of dataset, create its respective dataset in datasets/dataType.py

from datasets.base import BaseDataset
import json
from os.path import join # It’s used for safely combining folder paths and filenames since different OS use different separators.

class EarthVQADataset(BaseDataset):
  
    def __init__(self, image_dir, qa_path):
        self.image_dir = image_dir
        self.qa_path = qa_path

    def load(self):
        qas_dict = json.load(open(self.qa_path, "r"))
        new_evqa = []
        for imagen, qas_list in qas_dict.items(): # loop through each image
            for qa_dict in qas_list: # loop through all questions for that image

                sample = {
                    "image": join(self.image_dir, imagen),
                    "question": qa_dict["ques"],
                    "answer": qa_dict["ans"],
                    "question_type": qa_dict["questype"]
                }
                new_evqa.append(sample)
        return new_evqa
