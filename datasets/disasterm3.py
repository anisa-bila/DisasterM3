# DisasterM3 dataset class that handles loading and formatting the DisasterM3 specific JSON data
# For a different type of dataset, create its respective dataset in datasets/dataType.py

from datasets.base import BaseDataset
import json
from os.path import join

class DisasterM3Dataset(BaseDataset):
    
    def __init__(self, project_root, subset):
        self.project_root = project_root
        self.subset = subset
    
    def load(self):
        subset_json = join(self.project_root, "data", f"{self.subset}.json")
        with open(subset_json, "r") as f:
            ds = json.load(f)
        ds = [dict(id=f"{self.subset}_{data_idx}", **data_dict) 
              for data_idx, data_dict in enumerate(ds)]
        return ds
