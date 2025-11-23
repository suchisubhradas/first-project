print("Hi Prince")
import cv2

# Use raw string or double backslashes to avoid escape character issues
image = cv2.imread(r'C:\Users\User\Desktop\mummy-man-Egyptian-Ptolemaic-name-collection-Musee.jpg')

if image is None:
    print("Error: Image not found or the path is incorrect.")
else:
    # Display the image in a window
    cv2.imshow('Mummy Man', image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    # cv2.destroyAllWindows()

