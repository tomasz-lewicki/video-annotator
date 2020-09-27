import imageio
import cv2

reader = imageio.get_reader("in_small.mp4")
fps = reader.get_meta_data()["fps"]

writer = imageio.get_writer("out.mp4", fps=fps)

for im in reader:
    im2 = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    cv2.imshow("szo", im2)
    cv2.waitKey(1)
    writer.append_data(im[:, :, 1])
writer.close()
