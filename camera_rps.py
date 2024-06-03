import cv2
import numpy as np
import tensorflow.keras as keras

class RockPaperScissors:
    def __init__(self, model_path):
        self.model = keras.models.load_model(model_path)
        self.class_names = ['Rock', 'Paper', 'Scissors', 'Nothing']
        self.cap = cv2.VideoCapture(0)

    def get_prediction(self, frame):
        """
        Predict the gesture in the frame using the loaded model.
        
        Parameters:
            frame (ndarray): The image frame from the webcam.
        
        Returns:
            str: The predicted gesture.
        """
        image = cv2.resize(frame, (224, 224))
        image = np.expand_dims(image, axis=0)
        predictions = self.model.predict(image)
        return self.class_names[np.argmax(predictions[0])]

    def display_instructions(self, frame, text, countdown=None):
        """
        Display instructions and countdown on the webcam frame.
        
        Parameters:
            frame (ndarray): The current video frame.
            text (str): Text to display.
            countdown (int): Optional countdown to display.
        """
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        if countdown is not None:
            cv2.putText(frame, f"Starting in {countdown}...", (10, 100), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    def run(self):
        """
        Run the main event loop of the application.
        """
        countdown = 3
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Display instructions
            self.display_instructions(frame, 'Press "c" to capture, "q" to quit')

            # Show the frame
            cv2.imshow('Rock Paper Scissors', frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                for i in range(countdown, 0, -1):
                    self.display_instructions(frame, 'Get ready', i)
                    cv2.imshow('Rock Paper Scissors', frame)
                    cv2.waitKey(1000)

                # Capture and predict
                prediction = self.get_prediction(frame)
                print(f"Predicted Gesture: {prediction}")

            elif key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    game = RockPaperScissors('/path/to/your/model.h5')
    game.run()