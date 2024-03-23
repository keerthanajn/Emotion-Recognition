import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound
from deepface import DeepFace
import os



# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

last_detected_emotion = None

# Read frames from the camera and perform face recognition
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))



#     import mediapipe as mp

#     BaseOptions = mp.tasks.BaseOptions
#     FaceLandmarker = mp.tasks.vision.FaceLandmarker
#     FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
#     VisionRunningMode = mp.tasks.vision.RunningMode

#     options = FaceLandmarkerOptions(
#         base_options=BaseOptions(model_asset_path=model_path),
#         running_mode=VisionRunningMode.VIDEO)

#     with FaceLandmarker.create_from_options(options) as landmarker:
#     # The landmarker is initialized. Use it here.
#   # ...
#     mp_image    = mp.Image(image_format=mp.ImageFormat.SRGB, data=numpy_frame_from_opencv)
#     face_landmarker_result = landmarker.detect_for_video(mp_image, frame_timestamp_ms)



    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        y = int(y)
        x = int(x)
        h = int(h)
        roi_color = frame[y:y+h, x:x+w]

        try:
        #     # Perform emotion detection
            result = DeepFace.analyze(roi_color, actions=['emotion'])
            print (result)
            last_detected_emotion = result[0]['dominant_emotion']
            
        #     # Get the last detected emotion
            # last_detected_emotion = result['dominant_emotion']

        #     # Draw rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #     # Display emotion text on the frame
            # last_detected_emotion="test"
            cv2.putText(frame, f'Mood Detector: {last_detected_emotion}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
           


        except Exception as e:
            print(f"Error analyzing face: {e}")

    # Display the frame with face recognition
    cv2.imshow("Face Recognition APPLICATIONNNN", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        tts = gTTS(text=f'Your current mood is {last_detected_emotion}', lang='en')
        tts.save('emotion.mp3')
        os.system('mpg123 emotion.mp3')  # You might need to install mpg321 or use another player
        

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break

# Print the last detected emotion after the loop
print(f'Last Detected Emotion: {last_detected_emotion}')

# Release the camera when the script is terminated
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
