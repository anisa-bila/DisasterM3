## Recreate Minimal Execution

In this document, ```DisasterM3/pyscripts/run_vllm.py``` is executed to test and document for dependencies, execution steps, and potential issues. It is the main script that runs the actual inference stage, responsible for generating prompts by combining disaster images and textual data together. The script feeds disaster image-text pairs into the vision language models and saves their answers in the results file.

## Known Dependencies

### Module Installation
Many modules require installation to move forward with the script. Each module is allocated a different size. 

### Execution Steps
1. Open Windows Terminal
2. Run the code ```pip install Pillow tqdm transformers vllm```


### Encountered Issues
<img width="960" height="111" alt="Screenshot 2026-05-26 095833" src="https://github.com/user-attachments/assets/007a42db-de9a-45a9-8afc-3671c4bca419" />
To use this script on another client, it is necesssary to install them all at once to avoid getting repetitive errors as output. Additionally, VLLM and transformers packagers are especially huge packages that require a significant amount of storage space to install, taking time to download. 







  
