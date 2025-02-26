# PCOS Detection System

This project is a Streamlit-based web application that helps detect Polycystic Ovary Syndrome (PCOS) risk based on BMI, acne detection, and excessive hair growth. The application also includes an option for image upload or camera input for acne detection.

## Features

- Calculate BMI and classify into categories.
- Detect acne using a pre-trained model.
- Classify excessive hair growth based on user input.
- Analyze and display PCOS risk based on BMI, acne detection, and hair growth.

## Requirements

- Python 3.x
- Streamlit
- TensorFlow
- OpenCV
- NumPy
- Pillow

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/pcos-detection-system.git
    cd pcos-detection-system
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place the pre-trained acne detection model (`facemodel.h5`) in the project directory.

2. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

3. Open the provided URL in your web browser to access the application.

## How It Works

1. **User Inputs**: The user enters their weight, height, menstrual cycle length, and average sleep hours. They also provide information about acne and excessive hair growth.

2. **Image Input**: The user can upload an image or take a picture using the camera. The image is used for acne detection.

3. **BMI Calculation**: The application calculates the user's BMI based on the provided weight and height and classifies it into categories.

4. **Acne Detection**: The application uses a pre-trained model to detect acne from the uploaded or captured image.

5. **PCOS Risk Analysis**: The application analyzes the user's PCOS risk based on BMI, acne detection, and excessive hair growth. The result is displayed on the screen.

## Future Enhancements

- Improve the accuracy of acne and hair growth detection.
- Add more features for comprehensive PCOS risk assessment.
- Implement additional health metrics and lifestyle factors.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the
