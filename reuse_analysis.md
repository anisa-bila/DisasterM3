## The Current DisasterM3 Structure

The DisasterM3 repository has been updated with the datasets folder. Each time a new dataset is needed for the framework, more adjustments must be made in this folder, which can be inefficient. ```datasets/__init__.py``` would require additional new lines of code in the if/elif statement to accommodate the new dataset. On the other hand, ```datasets/disasterm3.py``` holds greater inefficiency since a whole new file must be written from scratch with its own completely independent field names to handle its own logic based on the dataset's criteria. 

## Reuse Analysis

EarthVQA is a Visual Question Answering (VQA) dataset that advances relational reasoning-based judging, counting, and comprehensive analysis to support VLM models (Wang et al., 2024).

The following Python code in the tree structure will be analyzed:

```
EarthVQA/
├── data/
│   ├── earthvqa.py
```
The file ```earthvqa.py``` uses the decorator ```@er.registry.DATALOADER.register()``` (line 135) on the ```EarthVQALoader``` class. The ```ever``` library is an external dependency installed through: ```pip install ever-beta```.

This decorator implements a reusable registry-based design. Whenever a new dataset is added, the data is automatically registered into a centralized registry managed by the ```ever``` library without  any manual modifications to the main training script. The data can be referenced and used by name.

The reusable registry-based design improves modularity because different datasets rely on incompatible formats and preprocessing methods. By enforcing a common interface for dataset loaders, ```ever-beta``` serves as an abstraction layer between datasets and the training pipeline. As a result, models and training code can be reusable without needing any major code rewrites for each additional dataset.

Using this registry pattern into DisasterM3's ```datasets/``` would eliminate the need for manual if/elif updates in ```datasets/__init__.py```. Each new dataset class would simply use the ```@er.registry.DATALOADER.register()``` decorator to register itself automatically, making the framework more scalable and reusable without modifying any existing code.



