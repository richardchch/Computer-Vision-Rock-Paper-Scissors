# Computer-Vision-Rock-Paper-Scissors

## AiCore Project

### Model Training Using Teachable Machine

## Table of Contents
- [Overview](#overview)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

## Overview
This project develops a machine learning model trained to recognize hand gestures for rock, paper, and scissors. Utilizing Google's Teachable Machine, this model leverages TensorFlow to provide a robust, web-integrated solution suitable for real-time applications.

## Description

### Training Process

#### Data Collection
- Collected images representing the three gestures: rock, paper, and scissors.
- Ensured diversity in the dataset by capturing images under various lighting conditions to enhance model robustness.

#### Model Setup
- Configured Teachable Machine to use the collected images for training a TensorFlow model.
- Provided customization options for training cycles and learning parameters adjustment.

#### Model Training
- Launched training via Teachable Machine, with real-time feedback on model performance and accuracy.
- Continuously monitored and adjusted parameters to improve results.

#### Model Evaluation
- Used Teachable Machine's validation tools to evaluate the model's accuracy.
- Made iterative adjustments to training data and parameters based on the insights.

#### Model Export
- Exported the fine-tuned model as a TensorFlow `.h5` file, ready for integration into web applications or platforms that support TensorFlow.

## Installation

### Getting Started

#### Prerequisites
- Ensure Python is installed on your machine. [Download Python](https://www.python.org/downloads/)
- TensorFlow is required to run the model. Install it using pip:
  ```bash
  pip install tensorflow
