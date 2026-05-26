from datasets.disasterm3 import DisasterM3Dataset

def build_dataset_config(dataset_name, project_root, subset):
    if "disasterm3" in dataset_name.lower():
        return DisasterM3Dataset(project_root, subset)
    else:
        raise NotImplementedError(dataset_name)
