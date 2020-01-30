import cv2
cam = cv2.VideoCapture(0)
s, img = cam.read()

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cuenta = 0

while s:
  cv2.imshow( winName,img )
  s, img = cam.read()
  key = cv2.waitKey(10)
  if key == ord('s'):
    cv2.imwrite("img"+str(cuenta)+".jpg", img)
    print("imagen guardada Numero")
    print(cuenta)
    cuenta = cuenta + 1
  if key == ord('q'):
    cv2.destroyWindow(winName)
    break

print ("Finalizado")
