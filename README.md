# Computer-Vision-Rock-Paper-Scissors

A machine learning-based project that recognizes hand gestures for "Rock, Paper, Scissors" using computer vision. The model, trained with Google's Teachable Machine, leverages TensorFlow for real-time gesture detection.

---

## Table of Contents
- [Overview](#overview)
- [Project Description](#project-description)
- [Training Process](#training-process)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

---

## Overview
This project uses machine learning and computer vision to create an interactive, gesture-based "Rock, Paper, Scissors" game. The model is trained to recognize hand gestures representing "rock," "paper," and "scissors" using a TensorFlow-based model from Teachable Machine. The result is a robust and real-time application suitable for educational and entertainment purposes.

---

## Project Description

### Training Process

#### Data Collection
- Captured images representing gestures for "rock," "paper," and "scissors."
- Enhanced dataset robustness by including diverse lighting conditions and backgrounds.

#### Model Setup
- Configured Google's Teachable Machine for training using the collected dataset.
- Tuned training cycles and learning parameters to optimize model performance.

#### Model Training
- Performed iterative training with real-time feedback on performance metrics such as accuracy and loss.
- Refined parameters and training data for continuous improvement.

#### Model Evaluation
- Utilized Teachable Machine's evaluation tools to assess model accuracy and reliability.
- Fine-tuned the dataset and retrained the model based on evaluation insights.

#### Model Export
- Exported the trained model as a TensorFlow `.h5` file for integration into Python-based applications or other TensorFlow-supported platforms.

---

## Installation

### Getting Started

#### Prerequisites
1. **Python**: Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/).
2. **TensorFlow**: Install TensorFlow to use the trained model:
   ```bash
   pip install tensorflow

### Setup
1. **Clone the repository to your local machine:**

   ```bash
   git clone https://github.com/richardchch/Computer-Vision-Rock-Paper-Scissors.git
   cd Computer-Vision-Rock-Paper-Scissors

   ```
2. **Install any additional dependencies, if required:**

   ```bash
   pip install -r requirements.txt

   ```

---

## Usage  

Clone the repository to your local machine:  
```bash
git clone https://github.com/richardchch/Computer-Vision-Rock-Paper-Scissors.git  
cd Computer-Vision-Rock-Paper-Scissors
```

### Run the camera_rps.py script to start the application:
`python camera_rps.py`

- Use your webcam to show gestures for "rock," "paper," or "scissors." The model will detect and classify the gestures in real time.

---

## File Structure
```bash

Computer-Vision-Rock-Paper-Scissors/  
 ├── camera_rps.py      # Gesture recognition script using the webcam and the trained model  
 ├── manual_rps.py      # Script for manual input-based Rock, Paper, Scissors gameplay  
 ├── keras_model.h5     # Trained TensorFlow model exported from Teachable Machine  
 ├── labels.txt         # Class labels corresponding to the model's output  
 └── README.md          # Documentation for the project

```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

- **Google's Teachable Machine**: For providing an intuitive interface for training machine learning models.
- **TensorFlow**: For the powerful tools enabling seamless integration of ML models into Python applications.

