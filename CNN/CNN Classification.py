import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing import image

# 1) Load CIFAR-10 data
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# 2) Normalize pixel values (0–255 -> 0–1)
train_images = train_images.astype("float32") / 255.0
test_images = test_images.astype("float32") / 255.0

# 3) One-hot encode labels (10 classes)
num_classes = 10
train_labels_cat = to_categorical(train_labels, num_classes)
test_labels_cat = to_categorical(test_labels, num_classes)

# 4) Define CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation="relu"),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(num_classes, activation="softmax")
])

# 5) Compile model  (typo fixed: loss, not lose)
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# 6) Train model
print("Training CNN model...")
history = model.fit(
    train_images,
    train_labels_cat,
    epochs=5,
    batch_size=64,
    validation_data=(test_images, test_labels_cat)
)

# 7) Load and preprocess your own image for prediction
img_path = "cat.jpg"

# Load and resize to 32x32 (same as CIFAR-10 images)
img = image.load_img(img_path, target_size=(32, 32))
plt.imshow(img)
plt.axis("off")
plt.show()

# Convert to array and normalize
img_array = image.img_to_array(img)
img_array = img_array.astype("float32") / 255.0
img_array = np.expand_dims(img_array, axis=0)  # shape: (1, 32, 32, 3)

# 8) Predict the class
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)[0]

# CIFAR-10 class names
class_names = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

print(f"Predicted class: {class_names[predicted_class]}")
