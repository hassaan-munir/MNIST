# MNIST Digit Recognition Project

![MNIST Sample](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)

A complete implementation of a Convolutional Neural Network (CNN) to recognize handwritten digits (0-9) from the MNIST dataset, with a simple Streamlit web interface.

## Features

* **98.25% Test Accuracy** on MNIST dataset
* **Interactive Streamlit Web App** for real-time predictions
* **Automatic Preprocessing**: image normalization and resizing
* **CNN Architecture**: 2 Convolutional Layers with MaxPooling, 2 Dense Layers with Dropout
* **Easy Deployment** with minimal dependencies

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/mnist-digit-recognition.git
cd mnist-digit-recognition
```

2. Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the web app:

```
streamlit run app.py
```

Train the model:

```
python train_model.py
```

## Model Architecture

```
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(100, activation='relu'),
    Dense(10, activation='softmax')
])
```

## Project Structure

```
.
├── app.py                # Streamlit web application
├── train_model.py        # Model training script
├── mnist_cnn_model.h5    # Pretrained model
├── requirements.txt      # Dependencies
└── README.md             # This file
```

## Future Improvements

* Multi-digit recognition
* Drawing canvas in web app
* Deploy as a REST API

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## Contact Me

Connect with me on LinkedIn: [Muhammad Hassaan Munir]((https://www.linkedin.com/in/muhammad-hassaan-munir-79b5b2327/))

## License

MIT License

## Live Demo

 Click [Here]((https://mnist-digit-recognitions.streamlit.app/))
