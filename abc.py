
import easyocr

import matplotlib.pyplot as plt
import cv2
image_path = 'C:\\Users\\Ritesh\\OneDrive\\Documents\\project_ty\\Car-Number-Plates-Detection-main\\plates\\scaned_img_6.jpg'
image = cv2.imread(r'C:\Users\Ritesh\OneDrive\Documents\project_ty\Car-Number-Plates-Detection-main\plates\scaned_img_6.jpg0')

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

# Read the image and perform OCR


# Print results
for (bbox, text, prob) in results:
    print(f"Text: {text}, Probability: {prob}")

# Load the image
image = cv2.imread(image_path)

# Loop over the results and draw bounding boxes and text
for (bbox, text, prob) in results:
    # Extract the bounding box coordinates
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = (int(top_left[0]), int(top_left[1]))
    bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

    # Draw the bounding box on the image
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

    # Put the OCR'd text on the image
    cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Display the image
cv2.imshow('Detected Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
