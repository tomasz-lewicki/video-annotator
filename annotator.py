import imageio
import cv2
import time
import json
import os

filename = "Fire_In_Santa_Rosa_at_Recycling_Facility_4k_Drone-5LtG-RGe4_g.mkv"
basename = filename.split(".")[0]

reader = imageio.get_reader(filename)
FPS = reader.get_meta_data()["fps"]
N = reader.count_frames()

WIN_WIDTH = 600
INTERVAL = round(FPS)

annotations = []


def exit_handler():
    with open(f"{basename}.json", "w") as f:
        f.write(json.dumps(annotations))


i = 0
for frame in reader:

    if i % INTERVAL == INTERVAL - 1:
        print(f"{i}/{N} ({i/N*100:.2f}%)")
        h, w, _ = frame.shape
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame = cv2.resize(frame, (WIN_WIDTH, int(h / w * WIN_WIDTH)))
        cv2.imshow("show frame", frame)
        key = cv2.waitKey(0) & 0xFF
        print(key)

        if key == 32:  # space (fire)
            annotations.append([i, 1])
        elif key == 8:  # backspace
            annotations.append([i, 0])
        elif key == ord("i"):  # invalid
            annotations.append([i, -1])
        elif key == ord("a"):  # ambiguous
            annotations.append([i, 2])
        elif key == ord("q"):  # quit
            exit_handler()
            exit(1)
    i += 1

exit_handler()
