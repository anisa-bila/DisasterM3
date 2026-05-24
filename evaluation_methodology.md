Vision Language Models are multimodal models that process both images and text to generate classified text outputs. They can assess a wide variety of images, including those depicting natural disasters.

## Nature of Data

Vision Language Models are trained on diverse datasets to pair high-quality images with rich textual descriptions. A varied dataset achieves optimal performance, eliminating generic outputs.

When especially used in the case of natural disasters, it is critical for the data to be clear with minimal errors since decisions are made fast and people's lives are at stake. High-quality data can help AI systems identify a crisis accurately and optimize coordination between emergency teams and humanitarian organizations.

**Image-text Pair**:

Image-text pair involves matching visual data with textual data. Their features are converted to numerical vectors in a common space called a shared embedding space, enabling comparison between image-text pairs.

Two types of data are critical for this training process:

  - **Image Data**: High-quality image datasets that cover an extensive range of objects and environments, enabling the model to examine and recognize different visual contexts.
	<br>
  - **Text Data**: Rich and diverse descriptive textual datasets such as captions, descriptions, or text that correspond accordingly to the paired image for analysis.

**Graph Question Answering Data**:

Designed to test the model's ability to answer multi-level questions about images. It enforces models to perform visual reasoning, using a structured map that connects the image's objects, their attributes, and the relationships between them to generate questions and answers.

Two types of data are critical for this training process:

  - **Annotated Data**: Used in outputs where models are given an image with a natural language question for scene or object interpretation, and they must produce an accurate answer. Often used for tasks like Graph Question Answering (GQA) and Visual Question Answering (VQA). (e.g., "What area is this?" - "A damaged forest.")

  - **Scene Graph Data**: Structured mappings that describe the objects in an image and their attributes, which encourages models to execute reasoning and understand the object's relationships with others.

**Other Types of Data Include**:

  - **Domain-specific Data**: Specialized datasets that help VLMs understand the link between an image and the given text the same way teams and organizations do. (e.g., A photo of earthquake damage - "Collapsed buildings observed, high-risk of injuries.")
  - **Web-Scale Data**: Billions of image-text pairs uploaded from the Internet into a large dataset to further expand concepts.
<br>

## Evaluation Metrics

Vision Language Models (VLMs) use several evaluation metrics that assess their capabilities in both understanding and integrating visual and textual data.

**Benchmark Datasets**

Different models are tested with standardized datasets with the purpose of challenging the model's reasoning and comprehension capabilities, often used as performance comparison between different models.
  <br>
- **Importance in Natural Disaster**: Benchmark datasets allow the team to compare performance across models to determine and select the most reliable model. A model with poor benchmarking often fails to translate real-world scenarios, bringing risks in a diaster scenario.
  
**Accuracy**
  
This metric determines how well the model can correctly associate images with their corresponding textual data.
   <br>
- **Importance in Natural Disaster**: The ability of models to accurately comprehend image-text association is highly critical, as a wrong comprehension could risk wrong emergency responses.
  
**Precision**

Measures how many of the model's output results are actually relevant and correct. A high precision score indicates the model avoids false detections.
     <br>
- **Importance in Natural Disaster**: Avoids flagging unharmed structures as damages to preserve resources and time for emergency responses that the team actually needs.
  
**Recall**

Captures the correct answers that exist within the dataset the model was able to successfully identify and generate.
  <br>
- **Importance in Natural Disaster**: Ensures no critical disaster areas or damages are missed, as overlooking affected parts could leave people without aid.
  
**F1 Score**

A balanced combination between precision and recall, useful for a dataset where the risks of false positives from incorrect outputs and false negatives from missed correct data are present.
  <br>
- **Importance in Natural Disaster**: THe presence of false positive or false negative in a disaster case can directly harm affected people by providing wrong emergency responses.
  
**Vector Quality**
A fundamental metric that involves analyzing the distance between vectors in a high-dimensional space, also known as a shared embedding space, to measure the similarity of relationships between them. Vectors that are close together indicate a  strong text-image link.
  <br>
- **Importance in Natural Disaster**: Helps the model associate a disaster visual data with its corresponding textual data. A flood image should link to a flood situation report to generate appropriate emergency measures.

  
