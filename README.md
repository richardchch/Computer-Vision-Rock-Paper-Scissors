# Computer-Vision-Rock-Paper-Scissors
AiCore Project


## Model Training Using Teachable Machine

### Overview
This project includes a machine learning model trained to recognize hand motions corresponding to rock, paper, and scissors. The model was developed using Google's Teachable Machine, an intuitive, web-based tool that allows for rapid model training with TensorFlow.

### Training Process
1. **Data Collection**: Collected images representing the three hand motions: rock, paper, and scissors. Each category was carefully captured under varying lighting conditions to enhance model robustness.

2. **Model Setup**: Configured Teachable Machine to train a TensorFlow model using the collected images. The interface provided options to set the number of training cycles and fine-tune the learning parameters.

3. **Model Training**: Initiated the training process in Teachable Machine. The real-time feedback allowed for monitoring the model's performance and accuracy throughout the training cycles.

4. **Model Evaluation**: Evaluated the model's accuracy using Teachable Machine's built-in validation tools. Adjustments were made to the training data and parameters based on the performance insights gained.

5. **Model Export**: Upon achieving satisfactory accuracy, the model was exported as a TensorFlow model, which can be integrated into web applications or other platforms supporting TensorFlow models.

### Usage
The trained TensorFlow model is included in this project and can be used to classify the hand motions of rock, paper, and scissors. Implementation details and example usage are provided in the subsequent sections of this documentation.

## Getting Started

### Prerequisites
- Ensure you have Python installed on your machine.
- TensorFlow library is required to run the model. Install it using pip:
  ```zsh
  pip install tensorflow
