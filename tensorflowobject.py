import threading

import cv2
from imageai.Detection import VideoObjectDetection
import os

# !!!Need to Download yolo-tiny.h5!!!


def forFrame(frame_number, output_array, output_count, detected_frame):
    try:
        print(frame_number)
        print(output_array)
        cv2.imshow('i', detected_frame)
        cv2.waitKey(1)
    except cv2.error as er:
        print(er.msg)


def detection(hello):
    print(hello)
    execution_path = os.getcwd()
    detector = VideoObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolo-tiny.h5"))
    detector.loadModel(detection_speed="fast")
    camera = cv2.VideoCapture(0)
    detector.detectObjectsFromVideo(camera_input=camera,
                                    save_detected_video=False, frames_per_second=100,
                                    per_frame_function=forFrame, minimum_percentage_probability=10,
                                    return_detected_frame=True)


t1 = threading.Thread(target=detection, args=("hello",))
t1.start()
