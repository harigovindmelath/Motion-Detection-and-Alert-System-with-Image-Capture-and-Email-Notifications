# Motion-Detection-and-Alert-System-with-Image-Capture-and-Email-Notifications
This Python project implements a real-time motion detection system using OpenCV. It captures video from a webcam, detects significant motion, and sends an email alert with an image of the detected motion. The program also includes functionality to clean up captured images after processing.
Here’s a description for a GitHub repository showcasing this project:
Motion Detection and Alert System with Image Capture and Email Notifications

This Python project implements a real-time motion detection system using OpenCV. It captures video from a webcam, detects significant motion, and sends an email alert with an image of the detected motion. The program also includes functionality to clean up captured images after processing.
Key Features
1. Real-Time Motion Detection

    Captures live video feed from the webcam.
    Processes video frames in grayscale with Gaussian blur to reduce noise.
    Compares frames to detect motion using:
        Frame differencing.
        Thresholding and dilation for highlighting motion areas.
        Contour detection to identify objects with significant movement.

2. Image Capture on Motion

    When motion is detected, the program:
        Draws a green rectangle around the detected object.
        Saves the frame with the detected motion as an image in the images/ directory.

3. Email Notification

    Sends an email alert with an image of the detected motion using a separate send_email module.
    Ensures the notification process runs in a separate thread to avoid interrupting the motion detection loop.

4. Automatic Image Cleanup

    Deletes all images in the images/ directory after sending the email.
    Runs the cleanup process in a separate thread to maintain efficiency.

5. User-Friendly Exit

    The system runs continuously and stops when the user presses the "q" key.

How It Works

  Initialization:
      Opens the webcam feed and initializes the first frame for motion detection.
      Continuously reads and processes new frames.

  Motion Detection:
      Detects motion by calculating the absolute difference between the current frame and the initial frame.
      Highlights areas of motion with bounding rectangles.

  Alert Trigger:
      If significant motion is detected:
          Saves the current frame to the images/ directory.
          Sends an email with the middle image (from all captured images).
      Starts the email sending and cleanup processes in parallel threads.

  Image Cleanup:
      Deletes all images from the images/ directory after sending the alert.

Setup Instructions

  Dependencies: Install the required Python libraries:

    pip install opencv-python

Create Directories:

  Ensure an images/ directory exists in the project folder to store captured frames temporarily.

Email Integration:

  Implement the send_email module to handle email sending (e.g., using SMTP).
  Configure email credentials and the recipient address in the send_email module.

Run the Script:

    python motion_detector.py
