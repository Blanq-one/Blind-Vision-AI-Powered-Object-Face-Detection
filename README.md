Object Detection for the Blind
📌 About the Project

The goal of this project is to create a vision-assistive tool for blind and visually impaired users. The system uses Haarcascade classifiers to detect faces and bodies in real-time and provides directional audio feedback to guide the user.

🔑 Features

Real-time object and face detection

Detection of full body and frontal faces using Haarcascade models

Directional guidance system (direction.py) to assist with navigation

Converts detected objects into audio alerts

Lightweight and can run on modest hardware (e.g., laptops, Raspberry Pi)

💡 Use Cases

Assisting blind individuals with safe navigation in daily life

Detecting people and objects in the user’s environment

Acting as a digital guide dog for mobility support

Can be extended to include object labeling and distance estimation

📂 Project Structure

app.py → main application logic

direction.py → navigation and directional assistance

haarcascade_frontalface_default.xml → face detection model

haarcascade_fullbody.xml → body detection model

Ref_image_face.jpg → reference sample image

📊 Results

Detects faces and bodies in real-time using webcam input

Provides directional guidance to alert the user about detected obstacles

Improves user independence by translating vision into audio cues

🔮 Future Enhancements

Add distance estimation to measure how far objects are

Integrate with wearable devices (smart glasses, Raspberry Pi with camera)

Extend detection to more objects (chairs, doors, vehicles, etc.)

Multilingual voice support for accessibility

🤝 Contributing

Contributions are welcome! Open issues for improvements or bug fixes, and submit pull requests with enhancements.

📜 License

This project is open-source and available under the MIT License.

✨ “Helping the blind see the world, one detection at a time.”
