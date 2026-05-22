Vision Language Models are multimodal models that process both images and text to generate classified text outputs. They can assess a wide variety of images, including those depicting natural disasters.

# Nature of Data

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
# Evaluation Metrics



  
