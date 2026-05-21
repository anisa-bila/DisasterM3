Vision Tasks - The difference between classification, detection, and segmentation.

1. **Classification**: Examines the whole image to classify and assign a suitable label for it. Image classification can highlight the visible disaster occuring without identifying the location.
   **Output**: A single label assigned to the given image
   **Example**: Flood assessment
   
3. **Detection**: Focuses on surrounding detected objects with colour-coded boxes to locate and find where they are. It is more informative compared to classification.
   **Output**: Boxes outlined around each detected object, where a label will be assigned.
   **Example**: A damaged house with wildfire spreading across trees.
   
5. **Segmentation**: Performs a pixel-level analysis that belongs to each detected object or category by outlining the actual shape of them. It is the most precise of the three, highlighting only the pixels belonging to the detected object and separating it from the background.
   **Output**: Detected objects are divided into segments with each having a colour-coded pixel mask.
   **Example**: A flood expanding across a neighbourhood.
