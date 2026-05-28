## The Current DisasterM3 Structure

DisasterM3 repository had been updated with the datasets folder. Each time a new dataset is needed for the framework, more adjustments must be made in this folder, which can be inefficient. ```datasets/__init__.py``` would require additional new lines of code in the if/elif statement to accomodate the new dataset. On the other hand, ```datasets/disasterm3.py``` holds greater inefficiency since a whole new file must be written from scratch with its own completely independent field names to handle its own logic based on the dataset's criteria. 

## Reuse Analysis

EarthVQA is a Visual Question Answering (VQA) dataset that advances relational reasoning-based judging, counting, and comprehensive analysis to support VLM models (Wang et al., 2024).

The following Python code in the tree structure will be analyzed:

```
EarthVQA/
├── data/
│   ├── earthvqa.py
```
The file ```earthvqa.py``` uses the decorator ```@er.registry.DATALOADER.register()``` (line 135) on the ```EarthVQALoader``` class. The ```ever``` library is an external dependency installed through: ```pip install ever-beta```.

This decorator implements a reusable registry-based design. Whenever a new dataset is added, the data is automatically registered into a centralized registry managed by the ```ever``` library without  any manual modifications to the main training script. The data can referenced and used by name.

The reusable registry-based design improves modularity because different datasets rely on incompatible formats and preprocessing methods. By enforcing a common interface for dataset loaders, ```ever-data```serves as an abstraction layer between datasets and the training pipeline. As a result, models and training code can be reusable without needing any major code rewrites for each additional dataset.

The proposed framework operates better without any specific hardcode variables. With a compatible loader, ```data-set``` acts as a framework with a registry system for dataset loaders that can be reusable.


