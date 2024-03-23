
# Face Recognition and Emotion Detection Application

This Python application utilizes **OpenCV**, **DeepFace**, and several other libraries to perform real-time face recognition and emotion detection using a webcam. It showcases the power of AI in understanding human emotions by analyzing facial expressions in real-time.

## Features

- Real-time face detection using **OpenCV**.
- Emotion detection leveraging **DeepFace's** deep learning models.
- Audible feedback on detected emotions using **Google's Text-to-Speech (gTTS)**.
- Designed to run with a computer's built-in or external webcam.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python 3.6** or higher installed.
- Access to a **webcam**.

## Installation

Clone this repository to your local machine:

```
git clone https://your-repository-url.git
cd your-project-directory
```

Install the required Python packages:

```
pip install opencv-python deepface gTTS playsound
```

**Note:** If you encounter a TensorFlow and keras version conflict as mentioned, you may need to adjust your TensorFlow version or install `tf-keras`:

```
pip install tf-keras
```

Alternatively, adjust your TensorFlow version according to the requirements of DeepFace:

```
pip install tensorflow==your_compatible_version
```

## Usage

To run the application, navigate to the project directory and execute:

```
python face_emotion_recognition.py
```

Press `q` to quit the application at any time.
Press `s` to listen to speech at any time.



## License

[MIT License](LICENSE.txt) - **Keerthana**
```
