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
