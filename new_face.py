import cv2

from names import add_name

camera = cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

name = input("Enter name: ")
id = add_name(name)
count = 0

while True:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    cv2.putText(frame, "Saving new face, please wait", (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 255, 255), 2)

    for (x, y, w, h) in faces:
        count = count + 1

        cv2.imwrite('datasets/User.' + str(id) + "." + str(count) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (222, 49, 99), 1)

    cv2.imshow("New face", frame)

    k = cv2.waitKey(1)

    if count > 100:
        break

camera.release()
cv2.destroyAllWindows()

print("Face recognition completed.")
