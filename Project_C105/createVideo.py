import os
import cv2

path = "images"
images = []
for file in os.listdir(path):
    name,extension = os.path.splitext(file)

    if extension in '.jpg':
        file_name = path + "/" + file
        #print(file_name)
        images.append(file_name)

count = len(images)
frame = cv2.imread(images[0])
width, height, channels = frame.shape
print((width,height))

output = cv2.VideoWriter('album.mp4',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))

for image in range(0,count-1):
    frame = cv2.imread(images[image])
    output.write(frame)

output.release()
print("Video created")