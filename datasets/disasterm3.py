# DisasterM3 dataset class that handles loading and formatting the DisasterM3 specific JSON data
# For a different type of dataset, create its respective dataset in datasets/dataType.py

from datasets.base import BaseDataset
import json
from os.path import join # It’s used for safely combining folder paths and filenames since different OS use different separators.

class DisasterM3Dataset(BaseDataset):
    
    def __init__(self, project_root, subset): # Self defines this specific object of the class, in this case the DisasterM3Dataset
        self.project_root = project_root
        self.subset = subset # The name of the .json file
    
    def load(self):
        subset_json = join(self.project_root, "data", f"{self.subset}.json") # join("C:/DisasterM3", "data", "test.json")
        with open(subset_json, "r") as f: # Opens the JSON file in read mode
            ds = json.load(f) # Conversion to allow Python to work on this file
        new_ds = [] # Stores the processed dataset items

        for data_idx, data_dict in enumerate(ds): # Loop through every dataset item while also tracking its index number
            # Enumerate gives the index number and item itself

            item = dict(
                id=f"{self.subset}_{data_idx}", # gives test_0, test_1, test_2... in which the json file name is test
                **data_dict # unpack/spread all dictionary contents here
            )

            new_ds.append(item)
    
        ds = new_ds
        return ds

