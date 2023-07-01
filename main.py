import cv2
import numpy as np
import time

# Параметры видео
width, height = 100, 100
fps = 30
duration = 3

# Создаем видео
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
video_number = int(time.time())
video_name = f"./videos/running_text{video_number}.avi"
video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

# Ввод текста с консоли
text = input("Введите текст для бегущей строки: ")

x = width
y = height // 2

# Настройки визуала
text_color = (255, 255, 255)
background_color = (0, 255, 0)

for frame_number in range(duration * fps):
    frame = np.full((height, width, 3), background_color, dtype=np.uint8)
    cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)
    video.write(frame)
    x -= 2

# Завершаем запись и закрываем
video.release()
cv2.destroyAllWindows()
