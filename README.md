# OpenPose
This repository is made for examples about [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) exercise.

<br><br>
## Installation
```
git clone https://github.com/esemeniuc/openpose-docker
cd openpose-docker
docker run -it --rm --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=0 cwaffles/openpose
```
If you got a error message like  
```docker: Error response from daemon: Unknown runtime specified nvidia.```,  
please use docker run -it --rm **--gpus all** -e NVIDIA_VISIBLE_DEVICES=0 cwaffles/openpose


<br><br>
## Requirement
1. You need the MPI and COCO models.  
   If you have a model that you have trained yourself through your algorithm, you can use it.
   * MPII Model: http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/mpi/pose_iter_160000.caffemodel
   * COCO Model: http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/coco/pose_iter_440000.caffemodel
   <br>
2. You need an OpenCV library to use that models.
   ```
   pip install opencv-python
   ```

<br><br>
## Getting Started
```
git clone https://github.com/kimkyeongnam/OpenPose.git
cd OpenPose

python /img/test.py        # check img file
python /video/testVIDEO.py  # check video file
```

<br><br>
## Result
### Image
![image](https://user-images.githubusercontent.com/38516906/74110804-df500480-4bd2-11ea-9137-ba5e597ff1a8.png)
