## Recreate Minimal Execution

In this document, ```DisasterM3/pyscripts/run_vllm.py``` is executed to test and document for dependencies, execution steps, and potential issues. It is the main script that runs the actual inference stage, responsible for generating prompts by combining disaster images and textual data together. The script feeds disaster image-text pairs into the vision language models and saves their generated answers into a results file.

## Known Dependencies

### Module Installation
Many Python modules require installation to move forward with the script. Each module varies in size and installation time.

Required modules include:

```pip install Pillow tqdm transformers vllm```

### Linux or Docker Required
The ```vllm``` module performs best in Linux or Docker environments. Linux is highly recommended and best-supported for vLLM, designed for high-performance server environments with GPU support.

### GPU Dependency
Models need GPUs for inference. QwenVL, InternVL, and Llava have billions of parameters that must be loaded into GPU memory to process and answer input questions. The largest models need multiple GPUs to work.

## Execution Steps
1. Open Windows Terminal.
2. Run ```pip install Pillow tqdm transformers vllm```
3. Run the ```run_vllm.py``` Python script.
4. Script fails because vLLM does not official support Windows environments.

## Encountered Issues
<img width="960" height="111" alt="Screenshot 2026-05-26 095833" src="https://github.com/user-attachments/assets/007a42db-de9a-45a9-8afc-3671c4bca419" />
To execute this script successfully on another client, it is necessary to install all required dependencies beforehand to avoid getting repetitive errors as output. Additionally, ```vllm``` and ```transformers``` packages are large libraries that require significant storage space and installation time.

<img width="1007" height="155" alt="image" src="https://github.com/user-attachments/assets/c5e8720f-f103-4acc-87a9-151dc15d6fc7" />
The ```vllm``` module does not officially support Windows. As a result, the script is unable to run properly without a proper OS environment like Linux or Docker for high-performance inference. Attempting to install or run the script directly on Windows will result in installation and execution errors.

## Suggested README Improvements
It's important for the README to have the necessary requirements for the user to prepare and ensure successful operations. Reproducing the execution without proper environments could be difficult for users with limited hardware resources or unsupported operating systems.

The README should include:
- Recommended Linux or Docker setup instructions/operating system compatibility notes
- Dependency packages requirement including ```Pillow tqdm transformers vllm```
- Common troubleshooting steps for installation failures





  
