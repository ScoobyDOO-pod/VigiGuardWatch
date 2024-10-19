#Padmini Poduri


#VigiGuard.py


#Inputs:
    # Weather APIs: Provide data on the current emergency (e.g., heatwave, storm, or flood).
    # Smoke sensor: Detects potential fires in the user’s vicinity.
    # Temperature sensor: Monitors ambient conditions for extreme cold or heat.
    # AI Translation: Captures user speech for translation and communication with responders.
    # GPS: Tracks location to ensure alerts are tailored to the user’s surroundings.


#Process:
    # Step-by-Step: Installing Libraries in Visual Studio Code
        # Open Visual Studio Code.
            # Activate the Terminal:
            # In VS Code, go to View > Terminal (or press Ctrl + ~ on Windows).
            # This will open the terminal at the bottom of the window.
            # Activate Your Virtual Environment:

        #On Windows:
        # .venv\Scripts\activate
        # Install the Required Libraries: Now, with the virtual environment active, enter the following command in the Terminal:
            # Install requests:
                # pip install requests
            # Install googletrans (specific version to avoid known issues):
                # pip install googletrans==4.0.0-rc1
            # Install geocoder:
                # pip install geocoder
            # Install playsound:
                # pip install playsound
                # pip install playsound==1.2.2
                # pip install pygame



        # Verify the Installation: After the installation completes, check if the libraries were installed successfully:
            # pip list

    #Weather Emergency Alert Handling:
        # The weather API sends data on a potential emergency (e.g., storm, flood, heatwave).
        # The AI model analyzes the situation and generates a customized checklist based on the event.
        # Example for flood:
        # "Move valuable items to higher ground."
        # "Prepare a go-bag with essentials."
        # "Avoid walking through floodwaters."
        # Translation Feature:


    # Language translation
        # The user types or speaks into the watch in their native language (e.g., "Ayuda").
        # The user can also choose a pre written prompt(e.g, " ayudame yo ....").
        # The AI translates the message into English and
        # plays it through the speaker and writes it. for emergency responders that the user calls
        # using ther phone.
            # The idea is that the user who doesn't know how to speak english in an emergency such
            # as domestic abuse will be prompted by the watch with AI a list of steps to do in this
            # emergency. Which includes calling 911. but since the user is a non english speaker
            # they might not be able to retale valuable information to emergency responders quickly
            #  through phone or text.  So when the user calls 911 as prompted he or she will say or
            #  type their emergency and the speaker will translate out loud so that the 911 people can
            # hear through the phone.the user can also choose a no sound option and copy and paste the
            # translated text to text 911 as well.


    # Sensor-Triggered Alerts:
        # Smoke sensor detects smoke and triggers vibrations and a fire alert.
        # Temperature sensor identifies dangerously hot or cold conditions and sends alerts to the user.
        # Blood pressure sensor will detect dangerous blood pressure conditions and send an alert.
        # stress sensor will detect high stress levels and will alert the user to take deep breaths.


    # Vibration Patterns:
        #Distinct vibration patterns are assigned to different emergencies:
        # Rapid pulses: Fire alert
        # Long bursts: Weather alert warning
        # Intermittent vibrations: Heatwave or cold alert




    # Checklist Management it is AI generated:
        # The to-do list for the emergency is displayed on the watch's OLED screen
        # and synced to the SafeSync app.
        # Users can mark items as complete via the app or watch interface.


    # Health and Battery Monitoring:
        #Continuous heart rate monitoring detects irregularities, sending notifications if needed.
        #The battery system ensures the user is notified in case of low power.


#Outputs:
    # Display:
        # "Type of emergency!":
        #   Checklist: 1. Move valuables. 2. Prepare go-bag. 3. Avoid floodwaters."
        #Health metrics such as steps, and heart rate.


    #Vibration Motor:
        #Short and quick pulses for fire alerts.
        #Longer bursts for severe weather events.


    # Speaker:
        # All emergecy situations along with vibrating will also say out loud
        # "Type of emergency situation" in the users selected language preference.
        # Audible prompts such as “Seek higher ground” or “Stay indoors.” in the users
        #  prefered language.
        # AI-translated messages spoken in English for responders.

# VigiGuard Watch + SafeSync App - Padmini Poduri

import requests
import geocoder
from googletrans import Translator
import pygame  # For sound playback
import time
import random  # Simulating sensor data

# Initialize pygame for audio alerts
pygame.mixer.init()

# Load sounds for different events
FIRE_ALARM_SOUND = "sounds/file_alarm.mp3"
FIRE_VIBRATION_SOUND = "sounds/Fire_vibration_pattern.mp3"
FLOOD_ALERT_SOUND = "sounds/floode_alert.mp3"
BATTERY_LOW_SOUND = "sounds/Battery_low.mp3"
STORM_WARNING_SOUND = "sounds/storm_warning.mp3"
HEATWAVE_WARNING_SOUND = "sounds/heatwave_warning.mp3"
COLD_ALERT_SOUND = "sounds/colde_alert.mp3"
SPEAK_NOW_SOUND = "sounds/speak_now.mp3"
IRREGULAR_HEARTBEAT_SOUND = "sounds/irregularheartbeat.mp3"
TAKE_BREATHS_SOUND = "sounds/take_breaths.mp3"
CHECKLIST_REMINDER_SOUND = "sounds/Checklist_reminder.mp3"
TASK_COMPLETED_SOUND = "sounds/Task marked as completed.mp3"
DEVICE_STARTUP_SOUND = "sounds/Device_startup.flac"
ERROR_ALERT_SOUND = "sounds/Error_alert.mp3"
NOTIFICATION_SOUND = "sounds/Notification.wav"
TEMP_VIBRATION_SOUND = "sounds/Temperature_vibration.mp3"
WEATHER_VIBRATION_SOUND = "sounds/Weather_vibration_pattern.mp3"

# Translator setup
translator = Translator()

# API URL (example for weather API - OpenWeatherMap)
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "8a780f7cff64e5ab3260fe6b5dcf0732"  

def get_weather(location):
    """Fetch weather data for the given location using OpenWeather API."""
    params = {"q": location, "appid": API_KEY, "units": "metric"}
    response = requests.get(WEATHER_API_URL, params=params).json()
    print(response)  # For debugging
    if response.get("weather"):
        weather = response["weather"][0]["description"]
        temp = response["main"]["temp"]
        return weather, temp
    else:
        return None, None


def translate_message(message, target_lang='en'):
    """Translate message to target language using googletrans."""
    translation = translator.translate(message, dest=target_lang)
    return translation.text

def play_sound(file):
    """Play sound using pygame."""
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def gps_location():
    """Fetch user's GPS coordinates."""
    g = geocoder.ip('me')
    return g.latlng

def emergency_checklist(emergency_type):
    """Generate an emergency checklist based on the type of emergency."""
    checklists = {
        "flood": [
            "Move valuables to higher ground.",
            "Prepare a go-bag with essentials.",
            "Avoid walking through floodwaters."
        ],
        "fire": [
            "Evacuate immediately.",
            "Call 911.",
            "Use a fire extinguisher if safe to do so."
        ],
        "heatwave": [
            "Stay indoors in air-conditioned areas.",
            "Drink plenty of water.",
            "Avoid outdoor activities during peak hours."
        ],
        "cold": [
            "Dress warmly and avoid prolonged exposure.",
            "Stay indoors and keep warm.",
            "Check on vulnerable neighbors."
        ]
    }
    return checklists.get(emergency_type, ["Stay safe!"])

def determine_emergency_type(weather, temp):
    """Determine the type of emergency based on weather conditions."""
    if "flood" in weather.lower():
        return "flood"
    elif "storm" in weather.lower() or "thunderstorm" in weather.lower():
        return "storm"
    elif temp > 35:
        return "heatwave"
    elif temp < 0:
        return "cold"
    else:
        return "normal"

def vibration_pattern(emergency_type):
    """Simulate vibration patterns for different emergencies and play the associated sound."""
    if emergency_type == "fire":
        print("Vibration: Rapid pulses (Fire alert)")
        play_sound(FIRE_VIBRATION_SOUND)  # Play vibration sound
        time.sleep(2)  # Wait for the vibration to finish
        play_sound(FIRE_ALARM_SOUND)  # Play the fire alarm sound
    elif emergency_type in ["storm", "flood"]:
        print("Vibration: Long bursts (Weather alert)")
        play_sound(WEATHER_VIBRATION_SOUND)
        time.sleep(2)  # Wait for the vibration to finish
        play_sound(STORM_WARNING_SOUND if emergency_type == "storm" else FLOOD_ALERT_SOUND)  # Play the respective warning sound
    elif emergency_type in ["heatwave", "cold"]:
        print("Vibration: Intermittent vibrations (Temperature alert)")
        play_sound(TEMP_VIBRATION_SOUND)
        time.sleep(2)  # Wait for the vibration to finish
        if emergency_type == "heatwave":
            play_sound(HEATWAVE_WARNING_SOUND)  # Play heatwave warning sound
        else:
            play_sound(COLD_ALERT_SOUND)  # Play cold alert sound

def sensor_alerts():
    """Simulate sensor alerts (fire, temperature, etc.)."""
    smoke_detected = random.choice([True, False])
    temp = random.uniform(-10, 45)  # Random temperature in Celsius

    if smoke_detected:
        print("Alert: Smoke detected! Evacuate immediately.")
        vibration_pattern("fire")
        play_sound(FIRE_ALARM_SOUND)

    if temp < 0 or temp > 35:
        print(f"Alert: Extreme temperature detected ({temp:.1f}°C).")
        vibration_pattern("heatwave" if temp > 35 else "cold")

def health_monitoring():
    """Simulate continuous health monitoring."""
    heart_rate = random.randint(60, 150)  # Random heart rate
    if heart_rate < 60 or heart_rate > 100:
        print(f"Alert: Abnormal heart rate detected ({heart_rate} BPM).")
        play_sound(IRREGULAR_HEARTBEAT_SOUND)

def main():
    print("VigiGuard Watch + SafeSync App Running...")
    play_sound(DEVICE_STARTUP_SOUND)

    # Fetch user's GPS location
    location = gps_location()
    print(f"Your location: {location}")

    # Get weather data for location
    weather, temp = get_weather("Miami")  # Example location
    print(f"Weather: {weather}, Temperature: {temp}°C")

    if weather and temp is not None:
        # Determine the type of emergency based on weather data
        emergency_type = determine_emergency_type(weather, temp)
        print(f"Emergency type determined: {emergency_type}")

        # Generate an emergency checklist based on the determined emergency type
        checklist = emergency_checklist(emergency_type)
        print(f"Checklist for {emergency_type.capitalize()}:\n" + "\n".join(checklist))
        play_sound(CHECKLIST_REMINDER_SOUND)

        # Simulate sensor alerts
        sensor_alerts()

        # AI Translation Example
        user_message = input("Enter a message for translation: ")
        translated_message = translate_message(user_message, 'en')
        print(f"Translated message: {translated_message}")
        play_sound(NOTIFICATION_SOUND)

        # Health monitoring example
        health_monitoring()
    else:
        print("Could not determine emergency type due to weather data unavailability.")

if __name__ == "__main__":
    main()
