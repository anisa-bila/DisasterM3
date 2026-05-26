## Recreate Minimal Execution

In this document, ```DisasterM3/pyscripts/run_vllm.py``` is executed to test and document for dependencies, execution steps, and potential issues. It is the main script that runs the actual inference stage, responsible for generating prompts by combining disaster images and textual data together. The script feeds disaster image-text pairs into the vision language models and saves their answers in the results file.

## Known Dependencies

### Module Installation
Many modules require installation to move forward with the script. Each module varies in size and installation time.. 

### Linux or Docker Required
VLLM module performs better in Linux or Docker environments. Linux is highly recommended and best-supported for vLLM, designed for high-performance server environments with GPU support.

### GPU Dependency
Models need GPUs for the inference process. QwenVL, InternVL, and Llava have billions of parameters that need to be loaded entirely into GPU memory to run and answer input questions. The largest models need multiple GPUs to work.

## Execution Steps
1. Open Windows Terminal
2. Run ```pip install Pillow tqdm transformers vllm```
3. Run the ```run_vllm.py``` Python script
4. Script fails due to vLLM not supporting Windows

## Encountered Issues
<img width="960" height="111" alt="Screenshot 2026-05-26 095833" src="https://github.com/user-attachments/assets/007a42db-de9a-45a9-8afc-3671c4bca419" />
To use this script on another client, it is necesssary to install them all at once to avoid getting repetitive errors as output. Additionally, VLLM and transformers packagers are especially huge packages that require a significant amount of storage space to install, taking time to download. 

<img width="1007" height="155" alt="image" src="https://github.com/user-attachments/assets/c5e8720f-f103-4acc-87a9-151dc15d6fc7" />
VLLM module does not support Windows. The script is unable to run without a proper OS environment like Linux or Docker for high-performance inference. Attempting to run the script on Windows will result in an installation error and the script will not execute.




  
