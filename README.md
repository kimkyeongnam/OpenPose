## Instructions
```
BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
              "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
              "Background": 15}

POSE_PAIRS = [["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
              ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
              ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"]]
```

1. WebCam (Using Ipad/Iphone cam as Ubuntu webcam)  
   * Description: https://steemit.com/technology/@tech.ninja/tech-quickie-convert-your-ipad-iphone-into-a-good-wireless-webcam-in-linux
   * Github Repository: https://github.com/umlaeute/v4l2loopback

2. Dependencies
   * Install all dependencies for [[tensorflow openpose]](https://github.com/ildoonet/tf-pose-estimation)
   * Download Model checkpoint with instructions from /models/graph/cmu/download.sh
   * Execute run_webcam.py to get real time inference
