## DisasterM3 Repository

**The Current Repository Structure**

As of now, the repository mainly consists of:

DisasterM3/
- The root of the repository

models/

├── __init__.py
- Processes images and videos, such as resizing the images or picking a few frames from a video, into format ideal for the model before feeding it with them.
- Inference implementations of three models: QwenVL, InternVL, Llava
- Specifies different format instructions these models prefer as input
     
pyscripts/

├── __init__.py
- An empty file that makes pyscripts a Python package

├── run_vllm.py
- Main script that runs the actual inference stage
- Prepares prompts about diaster images as input for the model
- The model's answers are saved in the results file

README.md

- Primary documentation for the repository as introdution and manual

__init__.py

- An empty file that makes pyscripts a Python package

analysis.md

- An analysis of the repository and the structure of the code

evaluation_methodology.md
- A documentation on how Vision Language Models are generally evaluated

vision_tasks.md
- A file that distinguishes between classifiction, detection, and segmentation
