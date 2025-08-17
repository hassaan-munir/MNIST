
# MNIST Digit Recognition Project

![MNIST Sample](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)

A complete implementation of a CNN model to recognize handwritten digits (0-9) from the MNIST dataset, with a user-friendly Streamlit web interface.

## Features

- **98.25% Test Accuracy** on MNIST dataset
- **Streamlit Web App** for real-time predictions
- **Preprocessing Pipeline**: Automatic image normalization and resizing
- **Model Architecture**: 
  - 2 Convolutional Layers + MaxPooling
  - 2 Dense Layers with Dropout
- **Easy Deployment**: Ready-to-use with minimal dependencies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mnist-digit-recognition.git
cd mnist-digit-recognition
Install dependencies:

bash
pip install -r requirements.txt
 Usage
Running the Web App:
bash
streamlit run app.py
Training the Model:
bash
python train_model.py
 Model Architecture
python
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(100, activation='relu'),
    Dense(10, activation='softmax')
])
 Project Structure
text
.
├── app.py                # Streamlit web application
├── train_model.py        # Model training script
├── mnist_cnn_model.h5    # Pretrained model
├── requirements.txt      # Dependencies
└── README.md            # This file
 Future Improvements
Add multi-digit recognition capability

Implement drawing canvas in the web app

Deploy as a REST API

 Contributing
Pull requests are welcome! For major changes, please open an issue first.

 License
MIT

text

### Key Highlights:
1. **Visual Appeal**: Added MNIST sample image at top
2. **Clear Structure**: Separated into logical sections
3. **Code Formatting**: Proper Markdown code blocks
4. **Future Scope**: Mentioned possible improvements
5. **Professional Touch**: Added license and contribution guidelines

You can copy-paste this directly into your README.md file. For better presentation:
- Add screenshots of your web app in an `/images` folder
- Include a demo GIF if possible
- Add badges for Python version, TensorFlow, etc.

Would you like me to add any specific details about your implementation or modify any section? 😊
