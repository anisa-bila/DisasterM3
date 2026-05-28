## Vision Language Model Evaluation Methodology

Vision Language Models (VLMs) are multimodal models that process both images and text to generate classified or descriptive text outputs. They can assess a wide variety of images, including those depicting natural disasters.

## Nature of Data

Vision Language Models are trained on diverse datasets to pair high-quality images with rich textual descriptions. A varied dataset achieves optimal performance, which reduces generic or inaccurate outputs.

When especially used in the case of natural disasters, it is critical for the data to be clear with minimal errors, since decisions must be made quickly and people's lives may be at stake. High-quality data helps AI systems identify crises accurately and improve coordination between emergency teams and humanitarian organizations.

**Image-text Pair**:

Image-text pairimg involves matching visual data with textual data. Their features are converted into numerical vectors within a common space called a shared embedding space, enabling comparison between image-text pairs.

Two types of data are critical for this training process:

  - **Image Data**: High-quality image datasets that cover an extensive range of objects and environments, enabling the model to examine and recognize different visual contexts.
	<br>
  - **Text Data**: Rich and diverse descriptive textual datasets such as captions, descriptions, or text that correspond accordingly to the paired image for analysis.

**Graph Question Answering Data**:

Graph Question Answering data is designed to test the model's ability to answer multi-level questions about images. It encourages models to perform visual reasoning using a structured map that connects the image's objects, their attributes, and the relationships between them to generate questions and answers.

Two types of data are critical for this training process:

  - **Annotated Data**: Used in outputs where models are given an image with a natural language question for scene or object interpretation, and they must produce an accurate answer. Often used for tasks like Graph Question Answering (GQA) and Visual Question Answering (VQA). (e.g., "What area is this?" - "A damaged forest.")

  - **Scene Graph Data**: Structured mappings that describe the objects in an image and their attributes, which encourages models to execute reasoning and understand the object's relationships with others in the scene.

**Other Types of Data Include**:

  - **Domain-specific Data**: Specialized datasets that help VLMs understand the relationship between images and the corresponding text in professional or operational contexts. (e.g., A photo of earthquake damage - "Collapsed buildings observed, high-risk of injuries.")
  - **Web-Scale Data**: Large-scale datasets containing billions of image-text pairs collected from the Internet to expand the mode's understanding of concepts.
<br>

## Evaluation Metrics

Vision Language Models (VLMs) use several evaluation metrics to assess their capabilities in both understanding and integrating visual and textual data.

**Benchmark Datasets**

- Different models are tested using standardized datasets with the purpose of challenging the model's reasoning and comprehension capabilities, often used to compare performance across models.
  <br>
- **Importance in Natural Disaster**: Benchmark datasets allow teams to compare model performance and select the most reliable model. A model with poor benchmarch performance may fail to translate real-world scenarios, increasing risks in a diaster scenario.
  
**Accuracy**
  
- This metric measures how well the model can correctly associate images with their corresponding textual data.
   <br>
- **Importance in Natural Disaster**: The ability of models to accurately comprehend image-text association is highly critical, as wrong comprehensions could lead to wrong emergency responses.
  
**Precision**

- Precision measures how many of the model's predicted outputs are actually relevant and correct. A high precision score indicates the model avoids false detections.
     <br>
- **Importance in Natural Disaster**: Avoids flagging unharmed structures as damages to preserve resources and time for emergency responses that the team actually needs.
  
**Recall**

- Recall measures how many relevant or correct outputs within the dataset were successfully identified by the model.
  <br>
- **Importance in Natural Disaster**: Ensures that critical disaster areas or damages are not missed, since overlooking affected regions could leave people without aid.
  
**F1 Score**

- The F1 Score is a balanced combination between precision and recall, making it useful for a dataset where the risks of false positives from incorrect outputs and false negatives from missed correct data are present.
  <br>
- **Importance in Natural Disaster**: False positives and false negatives in disaster scenarios can directly harm affected populations by causing incorrect or delayed emergency responses.
  
**Vector Quality**
- Vectory quality analyzes the distance between vectors in a high-dimensional space, also known as a shared embedding space, to measure the similarity of relationships between them. Vectors that are close together indicate a  strong text-image link.
  <br>
- **Importance in Natural Disaster**: Helps the model associate a disaster-related visual data with corresponding textual data. For example, a flood image should link closely to a flood situation report to support appropriate emergency measures.

  
