import cv2
import time
# import serial
# ser = serial.Serial('com5',9600)
# ser.timeout = 1



car_classifier = cv2.CascadeClassifier(r"C:/Users/Dell/PycharmProjects/car/cars.xml")

# Open two video capture objects

camera1 = cv2.VideoCapture(r"C:/Users/Dell/PycharmProjects/car/rightvideo.mp4")
camera2 = cv2.VideoCapture(r"C:/Users/Dell/PycharmProjects/car/leftvideo.mp4")

count1 = 0
count2 = 0
carCount_val =0



while camera1.isOpened() and camera2.isOpened():
    ret1, img1 = camera1.read()
    ret2, img2 = camera2.read()

    if not ret1 or not ret2:
        print("No frame found, exiting...")
        break

    # Process frames from the first video
    try:
        height1, width1 = img1.shape[:2]
        blur1 = cv2.blur(img1, (3, 3))
        gray1 = cv2.cvtColor(blur1, cv2.COLOR_BGR2GRAY)
        cars1 = car_classifier.detectMultiScale(gray1)
    except AttributeError:
        print("Error processing frame from video 1")
        continue

    cv2.putText(img1, 'Car COUNT: ' + str(count1), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    cv2.line(img1, (0, height1 - 200), (width1, height1 - 200), (0, 255, 255), 2)

    for (x, y, w, h) in cars1:
        car_cy = int(y + h / 2)
        lin_cy = height1 - 200

        if lin_cy - 6 < car_cy < lin_cy + 6:
            count1 += 1
            cv2.line(img1, (0, height1 - 200), (width1, height1 - 200), (0, 0, 255), 5)

        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img1, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Process frames from the second video
    try:
        height2, width2 = img2.shape[:2]
        blur2 = cv2.blur(img2, (3, 3))
        gray2 = cv2.cvtColor(blur2, cv2.COLOR_BGR2GRAY)
        cars2 = car_classifier.detectMultiScale(gray2)
    except AttributeError:
        print("Error processing frame from video 2")
        continue

    cv2.putText(img2, 'Car COUNT: ' + str(count2), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    cv2.line(img2, (0, height2 - 200), (width2, height2 - 200), (0, 255, 255), 2)

    for (x, y, w, h) in cars2:
        car_cy = int(y + h / 2)
        lin_cy = height2 - 200

        if lin_cy - 6 < car_cy < lin_cy + 6:
            count2 += 1
            cv2.line(img2, (0, height2 - 200), (width2, height2 - 200), (0, 0, 255), 5)

        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img2, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display processed frames
    cv2.putText(img1, 'Car COUNT: ' + str(count1), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    cv2.imshow('Video 1', img1)



    cv2.putText(img2, 'Car COUNT: ' + str(count2), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    cv2.imshow('Video 2', img2)

    carCount_val = carCount_val+1
    print(carCount_val)

    if(carCount_val>100):
        if (count1 > count2):

            # val = 'left'
            # val = val.strip()
            # ser.write(val.encode())
            # print(ser.readline().decode('ascii'))
            # time.sleep(0.3)
            print("70 percent green on left 30 percent red on left")

        else:
            # val = 'right'
            # val = val.strip()
            # ser.write(val.encode())
            # print(ser.readline().decode('ascii'))
            # time.sleep(0.3)
            print("70 percent green on right 30 percent red on right ")




    key = cv2.waitKey(1)
    if key == 27:  # press 'ESC' to exit
        break

cv2.destroyAllWindows()
camera1.release()
camera2.release()

