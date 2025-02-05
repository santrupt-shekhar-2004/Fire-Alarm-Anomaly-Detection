# Fire-Alarm-Anomaly-Detection
The complexity of modern fire hydrant systems presents several challenges when it comes to detecting system malfunctions or anomalies. Malfunctions such as pressure drops, leaks, valve failures, or unauthorized use of hydrants can go unnoticed until an emergency arises or significant water wastage occurs. Traditional rule-based monitoring systems rely on predefined thresholds or conditions to detect such issues. While effective to some extent, these systems are not equipped to handle new, evolving, or complex patterns in the data that may signal an impending failure.
For example, a sudden drop in water pressure may be interpreted as a routine fluctuation by a rule-based system if it falls within a predefined range. However, this could be an early sign of a larger issue, such as a developing leak or unauthorized tampering. The limitations of traditional systems call for a more dynamic and intelligent approach to anomaly detection—one that can analyze large volumes of data in real-time and adapt to changing patterns.
# Dataset Overview
The dataset consists of multiple environmental parameters that are critical for monitoring fire safety and detecting anomalies in fire suppression systems, such as sprinkler systems. The variables included in the dataset are:
1. Temperature:
   - Description: This variable measures the ambient temperature within a designated area (e.g., a room or building) and is typically recorded in degrees Celsius (°C) or Fahrenheit (°F).
   - Importance: Elevated temperatures are often an indicator of fire activity or potential fire hazards. Monitoring temperature changes is crucial for early detection of fires, as fires typically increase the surrounding temperature rapidly.
2. Smoke Density:
   - Description: This variable quantifies the concentration of smoke particles in the air, often expressed in terms of density or percentage. It can be measured using smoke detectors that use optical or ionization technologies.
   - Importance: Smoke density is a critical factor in fire detection systems. An increase in smoke density may signify the presence of fire, making it an essential parameter for real-time anomaly detection.
3. Humidity:
   - Description: Humidity represents the amount of moisture in the air, expressed as a percentage (%). It is measured using hygrometers or humidity sensors.
   - Importance: Humidity can affect fire behavior and the effectiveness of firefighting efforts. High humidity levels can slow down the spread of fire, while low humidity can accelerate it. Monitoring humidity levels helps assess the fire risk in a given environment.
4. Room Pressure:
   - Description: This variable measures the air pressure within a room or building, usually reported in pascals (Pa) or millibars (mbar).
   - Importance: Room pressure can influence the spread of smoke and gases during a fire. Understanding pressure changes can aid in evaluating fire dynamics and airflow patterns, which are essential for effective fire management and evacuation strategies.
5. CO2 Level:
   - Description: This parameter measures the concentration of carbon dioxide (CO2) in the air, typically expressed in parts per million (ppm). CO2 sensors monitor changes in CO2 levels due to combustion processes.
   - Importance: Increased CO2 levels can indicate the presence of a fire, as combustion releases CO2. Continuous monitoring of CO2 levels is vital for detecting and responding to fire incidents quickly.
6. Light Intensity:
   - Description: Light intensity measures the amount of light present in a given area, expressed in lux or lumens. Light sensors are employed to capture this data.
   - Importance: Changes in light intensity may signify a fire (e.g., flames producing light) or may affect the performance of smoke detectors. Monitoring light levels can provide additional context for fire detection systems.
7. Temperature-Smoke Interaction:
   - Description: This derived variable may represent the relationship between temperature and smoke density, capturing how temperature changes may correlate with variations in smoke levels.
   - Importance: Analyzing this interaction can help refine anomaly detection by identifying thresholds where significant deviations from normal behavior occur, indicating potential fire incidents
