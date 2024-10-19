
# VigiGuard Watch + SafeSync App

## Overview

**VigiGuard** is an innovative emergency alert and health monitoring application designed to enhance personal safety. By utilizing real-time weather data, location services, and sensor inputs, VigiGuard provides timely alerts for potential emergencies and health issues, ensuring users can respond effectively.

## Features

- **Emergency Alerts**: Monitors weather conditions to identify emergencies (e.g., floods, heatwaves) and provides customized checklists.
- **Health Monitoring**: Continuously tracks heart rate and alerts users to abnormal readings.
- **AI Translation**: Translates user messages to facilitate communication with emergency responders.
- **Vibration Alerts**: Distinct vibration patterns for different emergencies ensure users are aware even in noisy environments.
- **Checklist Management**: Displays actionable to-do lists for various emergencies, synced with the SafeSync app.

## Installation

### Prerequisites

- Python 3.x
- PIP (Python package installer)

### Installing Required Libraries

1. Open Visual Studio Code and activate the terminal (View > Terminal or Ctrl + ~).
2. Activate your virtual environment (e.g., `.venv\Scripts\activate` on Windows).
3. Install the required libraries:

   ```bash
   pip install requests
   pip install googletrans==4.0.0-rc1
   pip install geocoder
   pip install pygame
   ```

4. Verify installation:

   ```bash
   pip list
   ```

## Usage

1. Run the application:

   ```bash
   python VigiGuard.py
   ```

2. The app will fetch the user's GPS location and weather data, then monitor sensors and provide alerts as necessary.

3. Users can enter messages for translation, receive emergency checklists, and be alerted to health issues.

## How It Works

- **Weather Data**: Fetches real-time weather data to assess potential emergencies based on the user's location.
- **Sensor Integration**: Monitors smoke and temperature sensors for fire hazards and extreme weather conditions.
- **Health Metrics**: Continuously checks heart rate, sending alerts for irregularities.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
