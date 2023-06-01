import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("output",img)

cv2.waitKey(0)

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            3,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            5,
            (255,255,255)
            )

cv2.putText(img,
            "Venus",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            5,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            5,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            5,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            100,
            (255,255,255)
            )

