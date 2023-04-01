import cv2
import random
import os


def generateRandomIndex(count):
    start = [0, int(count/2/2), int(count/2), int(count/2/2*3), int(count-1)]
    frameNums = []
    for i in range(len(start)-1):
        j = 0
        while j < 3:
            rand = random.randint(start[i], start[i+1])
            if rand not in frameNums:
                frameNums.append(rand)
                j += 1
    return frameNums


print('Loading video files from /videos')
dir = './videos'
files = os.listdir(dir)
if (len(files) > 0):
    print('Found ' + str(len(files)))
    for file in files:
        vidcap = cv2.VideoCapture("./videos/" + file)
        totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        print("File: " + file + "\t Frame numbers: " + str(totalFrames))
        frameNums = generateRandomIndex(totalFrames)
        for i in range(len(frameNums)):
            vidcap.set(cv2.CAP_PROP_POS_FRAMES, frameNums[i])
            success, frame = vidcap.read()
            cv2.imwrite("./frames/" + file.partition('.')
                        [0] + '-' + str(i) + ".jpg", frame)
        vidcap.release()
        cv2.destroyAllWindows()
else:
    print("Found 0 file, exit")