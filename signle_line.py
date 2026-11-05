import cv2

car_classifier = cv2.CascadeClassifier(r"C:/Users/Dell/PycharmProjects/car/cars.xml")
camera = cv2.VideoCapture(r"C:/Users/Dell/PycharmProjects/car/leftvideo.mp4")

count = 0

while camera.isOpened():
    ret, img = camera.read()
    if not ret:
        print("No frame found, exiting...")
        break

    try:
        height, width = img.shape[:2]
    except AttributeError:
        print("Shape not found")
        continue

    cv2.putText(img, 'Car COUNT: ' + str(count), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    cv2.line(img, (0, height - 200), (width, height - 200), (0, 255, 255), 2)

    try:
        blur = cv2.blur(img, (3, 3))
        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        cars = car_classifier.detectMultiScale(gray)
    except cv2.error:
        print("Error processing frame")
        continue

    for (x, y, w, h) in cars:
        car_cy = int(y + h / 2)
        lin_cy = height - 200

        if lin_cy - 6 < car_cy < lin_cy + 6:
            count += 1
            cv2.line(img, (0, height - 200), (width, height - 200), (0, 0, 255), 5)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    try:
        cv2.imshow('image', img)
    except cv2.error:
        print("Error displaying frame")
        break

    key = cv2.waitKey(1)
    if key == 27:  # press 'ESC' to exit
        break

cv2.destroyAllWindows()
camera.release()
