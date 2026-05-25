## The Current Repository Structure

As of now, the repository mainly consists of:

```text
DisasterM3/
│   The root of the repository
│
├── models/
│   ├── \_\_init\_\_.py
│   │   Inference implementations of three models: QwenVL, InternVL, and Llava
│
├── pyscripts/
│   ├── \_\_init\_\_.py
│   │   An empty file that makes pyscripts a Python package
│   ├── run_vllm.py
│   │   Main script that runs the actual inference stage
│
├── README.md
│   Primary documentation for the repository, including introduction and usage instructions
│
├── \_\_init\_\_.py
│   An empty file that makes the root a Python package
│
├── analysis.md
│   Analysis of the repository structure and code organization
│
├── evaluation_methodology.md
│   Documentation describing how Vision Language Models are generally evaluated
│
└── vision_tasks.md
    Explains the differences between classification, detection, and segmentation tasks
```

## Code Organization Analysis #1

```
DisasterM3/
├── models/
│   ├── \_\_init\_\_.py
```

The ```models/``` package is responsible for preprocessesing videos and images into an ideal format for the model before feeding it with them. The script is designed to format different instructions for diverse models prefer as input.

The whole script consists of two sections:

### Preprocessing
The preprocessing pipeline includes:

- Detecting whether the input contains an image or a video
- Extracting a few still frames if a video was provided.
- Resizing images to fit the model's input preference in the right color format.
- Finding closest aspect ratios to the image's original proportions to avoid distortion.

### Formatting
- Initially runs the tokenizer of each model to convert text into numbers.
- Sets up each model's configuration (max tokens, max frames, number of GPUs).
- Combines the preprocessed images/video together with the text questions into a specific input structure each model prefers.

## Code Organization Analysis #2

```
DisasterM3/
├── pyscripts/
│   ├── run_vllm.py
```

The ```pyscripts``` package is the main script that runs everything, prepares prompts about disaster images as input for the model. The model's answers are saved in the results file.

This main script includes:

- ```prompt_libs```, a collection of blank question templates covering different disaster assessment tasks such as damage description and recovery recommendations, which later get filled with relevant pre-disaster and post-disaster images and questions.
- ```get_messages_from_data``` fills the templates with actual disaster images and questions from the dataset for the model to answer.
- Finalization of the script involves loading the disaster dataset, feeding it in batches through the model, and saving the answers to a result file.

## The Limitations

### Difficult to Maintain
The script, ```disasterm3/models/\_\_init\_\_.py```, has huge blocks of code with different kinds of functions designed for each model. It would take time to find a specific variable or function in the script to make adjustments.

### Lack of Standardization
Each model has its own way of accepting a format and input, with some functions serving only a single model. Adding a new model means writing a whole new functionw with its own formatting logic from scratch.

### Duplicated Logic
Some preprocessing and evaluation logic appears duplicated across scripts instead of a centralized reusable modules that can be used by all models.

## Framework Tied to DisasterM3
The script, ```disasterm3/pyscripts/run_vllm.py```, reads a JSON file with specific fields and data that are designed specifically for DisasterM3. Other datasets would need refining. Models are strictly evaluated with only this dataset with this hardcode format.





