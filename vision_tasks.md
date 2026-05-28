## Vision Tasks - The difference between classification, detection, and segmentation.

These three objectives are fundamental in computer vision. Each of them detect objects and provide details with different levels of precision. They are used in natural disasters to automatically monitor and analyze damage assessment, allowing the optimization of rescue operations.

1. **Classification**: Examines the whole image to classify and assign a suitable label for it. Image classification can highlight the visible disaster occuring without identifying its exact location.
   <br>
   - **Output**: A single label assigned to the given image (e.g, "Flood", "Earthquake Damage")
   - **Natural Disaster Use Case**: Assesses the type of disaster visible in the image. It identifies whether the crisis is a wildfire, landslide, or another type of natural disaster.
   
3. **Detection**: Focuses on surrounding detected objects with colour-coded boxes to locate and find where they are. It is more informative compared to classification.
   <br>
   - **Output**: Boxes outlined around detected objects, with a label will be assigned to each object.
   - **Natural Disaster Use Case**: Identifies and locates damaged infrastructure and disaster-related objects, such as collapsed buildings or wildfire spreading across trees.
   
5. **Segmentation**: Performs pixel-level analysis by assigning each pixel to a detected object or category, outlining the actual shape of the objects. It is the most precise of the three tasks, highlighting only the pixels belonging to the detected object and separating it from the background.
   <br>
   - **Output**: Detected objects are divided into segments with each having a colour-coded pixel mask.
   - **Natural Disaster Use Case**: Maps the exact pixels of a floodwater expanding across a neighbourhood, enabling precise estimation of the damaged areas.
