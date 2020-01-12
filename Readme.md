# Let's learn docker

Docker Engine is a client-server application with these major components:

* A server which is a type of long-running program called a daemon process (the dockerd command).
* A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.
* A command line interface (CLI) client (the docker command).

![](https://docs.docker.com/engine/images/engine-components-flow.png)

The CLI uses the Docker REST API to control or interact with the Docker daemon through scripting or direct CLI commands. Many other Docker applications use the underlying API and CLI.

The daemon creates and manages Docker objects, such as images, containers, networks, and volumes.

```Note: Docker is licensed under the open source Apache 2.0 license.```

![](https://docs.docker.com/engine/images/architecture.svg)

## The Docker daemon
The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.

## The Docker client
The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

# The underlying technology
Docker is written in Go and takes advantage of several features of the Linux kernel to deliver its functionality.

<img src="https://docs.docker.com/images/Container%402x.png" width=300 height=300>
<img src="https://docs.docker.com/images/VM%402x.png" width=300 height=300>


## Namespaces
Docker uses a technology called namespaces to provide the isolated workspace called the container. When you run a container, Docker creates a set of namespaces for that container.

These namespaces provide a layer of isolation. Each aspect of a container runs in a separate namespace and its access is limited to that namespace.

Docker Engine uses namespaces such as the following on Linux:

* The `pid` namespace: Process isolation (PID: Process ID).
* The `net` namespace: Managing network interfaces (NET: Networking).
* The `ipc` namespace: Managing access to IPC resources (IPC: InterProcess Communication).
* The `mnt` namespace: Managing filesystem mount points (MNT: Mount).
* The `uts` namespace: Isolating kernel and version identifiers. (UTS: Unix Timesharing System).

## Control groups
Docker Engine on Linux also relies on another technology called control groups (cgroups). A cgroup limits an application to a specific set of resources. Control groups allow Docker Engine to share available hardware resources to containers and optionally enforce limits and constraints. For example, you can limit the memory available to a specific container.

## Union file systems
Union file systems, or UnionFS, are file systems that operate by creating layers, making them very lightweight and fast. Docker Engine uses UnionFS to provide the building blocks for containers. Docker Engine can use multiple UnionFS variants, including AUFS, btrfs, vfs, and DeviceMapper.

## Container format
Docker Engine combines the namespaces, control groups, and UnionFS into a wrapper called a container format. The default container format is libcontainer. In the future, Docker may support other container formats by integrating with technologies such as BSD Jails or Solaris Zones.



# Let us dockerize my `Linear Regression code` in my [LinearRegression](https://github.com/junawaneshivani/LinearRegression/) repo.

```shivani@shivani-VirtualBox:~/Work/docker-tutorial$ sudo docker build -t linear-regression .
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
Normal Equation, theta0: 11.09, theta1: 1.27, accuracy 96.69```

