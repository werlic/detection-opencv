import cv2 as cv

img_path = 'test/test.png'

# Read image from your local file system
original_image = cv.imread(img_path)

# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2RGB)

# Load the classifier and create a cascade object for face detection
cascade_path = 'cascade/haarcascade_frontalface_alt.xml'
cascade = cv.CascadeClassifier(cascade_path)

detected_object = cascade.detectMultiScale(grayscale_image)

for (column, row, width, height) in detected_object:
  cv.rectangle(
    original_image,
    (column, row),
    (column + width, row + height),
    (0, 255, 0),
    2
  )

cv.imshow('Image', original_image)
cv.waitKey(0)
cv.destroyAllWindows()
