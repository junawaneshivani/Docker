### Let us dockerize my `Linear Regression code` in my [LinearRegression](https://github.com/junawaneshivani/LinearRegression/) repo.

```
shivani@shivani-VirtualBox:~/Work/docker-tutorial$ sudo docker build -t linear-regression .
Sending build context to Docker daemon  49.66kB
Step 1/5 : FROM ubuntu:18.04
 ---> 549b9b86cb8d
Step 2/5 : MAINTAINER junawaneshivani@gmail.com
 ---> Using cache
 ---> bc2686b7f369
Step 3/5 : RUN apt-get update -y &&     apt-get install -y python3-pip &&     pip3 install sklearn matplotlib pandas
 ---> Using cache
 ---> 707b27b2310f
Step 4/5 : COPY LinearRegression.py /
 ---> Using cache
 ---> c995fcfbdf78
Step 5/5 : CMD ["/bin/bash"]
 ---> Using cache
 ---> b955d855d6f5
Successfully built b955d855d6f5
Successfully tagged linear-regression:latest
shivani@shivani-VirtualBox:~/Work/docker-tutorial$ sudo docker run -it -d --name linear-regression linear-regression:latest
50d28eb15c3a83dda64f02ab4bab260695d6fc43f19ef3f621d3aca6186070ec
shivani@shivani-VirtualBox:~/Work/docker-tutorial$ sudo docker cp data.csv linear-regression:/data.csv
shivani@shivani-VirtualBox:~/Work/docker-tutorial$ sudo docker exec -it linear-regression python3 LinearRegression.py
Normal Equation, theta0: 11.09, theta1: 1.27, accuracy 96.69
```

