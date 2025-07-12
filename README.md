# AI-Powered Robotic Object Tracker

A Python-based project that performs real-time object detection and generates simulated movement commands for robotic alignment. The application uses OpenCV to process video input from a webcam and detect target objects, calculating positional offsets to determine directional commands.

## Features
- Live video feed processing
- Object detection with Haar Cascade classifiers
- Calculates object position relative to the frame center
- Generates commands: MOVE LEFT, MOVE RIGHT, FORWARD
- Visual overlays for detection and alignment

## Installation

Clone the repository and install dependencies:

```bash
cd ai-robot-object-tracker
pip install -r requirements.txt
