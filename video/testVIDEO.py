import cv2
import time
import numpy as np
import os

def proc(module, video):
    # MPII에서 각 파트 번호, 선으로 연결될 POSE_PAIRS
    """
    BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                  "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                  "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                  "Background": 15}

    POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                  ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                  ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                  ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]
    """

    if module is "coco":
        protoFile = "./model/coco.prototxt"
        weightsFile = "./model/coco.caffemodel"
        nPoints = 18
        POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]

    elif module is "mpi":
        protoFile = "C:\\Users\\kkyy0\\Desktop\\test\\venv\\MyScript\\pose_deploy_linevec_faster_4_stages.prototxt"
        weightsFile = "C:\\Users\\kkyy0\\Desktop\\test\\venv\\MyScript\\pose_iter_160000.caffemodel"
        nPoints = 15
        POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
    inWidth = 368
    inHeight = 368
    threshold = 0.1
    input_source = "C:\\Users\\kkyy0\\Desktop\\test\\venv\\MyScript\\video.avi"
    print(input_source)
    cap = cv2.VideoCapture(input_source)

    hasFrame, frame = cap.read()
    vid_writer = cv2.VideoWriter(video.split(".")[0] + "_"+ module + '.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame.shape[1],frame.shape[0]))
    net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
    while cv2.waitKey(1) < 0:
        t = time.time()
        hasFrame, frame = cap.read()
        frameCopy = np.copy(frame)
        if not hasFrame:
            cv2.waitKey()
            break
        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                                  (0, 0, 0), swapRB=False, crop=False)
        net.setInput(inpBlob)
        output = net.forward()
        H = output.shape[2]
        W = output.shape[3]
        points = []
        for i in range(nPoints):
            probMap = output[0, i, :, :]
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
            x = (frameWidth * point[0]) / W
            y = (frameHeight * point[1]) / H
            if prob > threshold :
                cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
                points.append((int(x), int(y)))
            else :
                points.append(None)
        for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]
            if points[partA] and points[partB]:
                cv2.line(frame, points[partA], points[partB], (0, 255, 255), 3, lineType=cv2.LINE_AA)
                cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
        cv2.putText(frame, "Test Time = {:.2f} sec".format(time.time() - t), (50, 50), cv2.FONT_HERSHEY_COMPLEX, .8, (255, 50, 0), 2, lineType=cv2.LINE_AA)
        vid_writer.write(frame)
    vid_writer.release()
    print("Fin Detect")

if __name__ == '__main__':
    module = ["mpi","coco"]
    proc("mpi", "avi")