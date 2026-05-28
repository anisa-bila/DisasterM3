## The Current DisasterM3 Structure

DisasterM3 repository had been updated with the datasets folder. Each time a new dataset is needed for the framework, more adjustments must be made in this folder, which can be inefficient. ```datasets/__init__.py``` would require additional new lines of code in the if/elif statement to accomodate the new dataset. On the other hand, ```datasets/disasterm3.py``` holds greater inefficiency since a whole new file must be written from scratch with its own completely independent field names to handle its own logic based on the dataset's criteria. 

## Reuse Analysis

The following Python code in the tree structure will be analyzed:

```
EarthVQA/
├── data/
│   ├── earthvqa.py
```


