Vision Tasks - The difference between classification, detection, and segmentation.

These three objectives are fundamental in computer vision. Each of them detect objects and provide details with precision in their own levels. They are used in natural disasters to automatically monitor and analyze damage assessment, allowing optimization of rescue operations.

1. **Classification**: Examines the whole image to classify and assign a suitable label for it. Image classification can highlight the visible disaster occuring without identifying the location.
   <br>
   **Output**: A single label assigned to the given image (e.g, "Flood", "Earthquake Damage")
   <br>
   **Natural Disaster Use Case**: Assesses the type of disaster visible in the image. It identifies whether the crisis is a wildfire, landslide, or any other detected natural disaster.
   
3. **Detection**: Focuses on surrounding detected objects with colour-coded boxes to locate and find where they are. It is more informative compared to classification.
   <br>
   **Output**: Boxes outlined around detected objects, where a label will be assigned to each.
   <br>
   **Natural Disaster Use Case**: Identifies and locates damaged infrastructure and the natural disaster detected, such as collapsed buildings or wildfire spreading across trees.
   
5. **Segmentation**: Performs a pixel-level analysis that belongs to each detected object or category by outlining the actual shape of them. It is the most precise of the three, highlighting only the pixels belonging to the detected object and separating it from the background.
   <br>
   **Output**: Detected objects are divided into segments with each having a colour-coded pixel mask.
   <br>
   **Natural Disaster Use Case**: Maps the exact pixels of a flood expanding across a neighbourhood, enabling precise estimation of the damaged areas.
