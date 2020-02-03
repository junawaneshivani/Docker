### CMD ["python","app.py"]
CMD is the command that is executed when you start a container. Here, you are using CMD to run your Python applcation.
There can be only one CMD per Dockerfile. If you specify more than one CMD, then the last CMD will take effect.

### COPY app.py /app.py
This line copies the app.py file in the local directory (where you will run docker image build) into a new layer of the image. This instruction is the last line in the Dockerfile. Layers that change frequently, such as copying source code into the image, should be placed near the bottom of the file to take full advantage of the Docker layer cache. This allows you to avoid rebuilding layers that could otherwise be cached. For instance, if there was a change in the FROM instruction, it will invalidate the cache for all subsequent layers of this image


And there you have it: a very simple Dockerfile. See the [full list of commands](https://docs.docker.com/engine/reference/builder/) that you can put into a Dockerfile. Now that you've defined the Dockerfile, you'll use it to build your custom docker image.


`$ docker image build -t python-hello-world .`

`$ docker image ls`

### Run the Docker image:

`$ docker run -p 5001:5000 -d python-hello-world`

The -p flag maps a port running inside the container to your host. In this case, you're mapping the Python app running on port 5000 inside the container to port 5001 on your host. Note that if port 5001 is already being used by another application on your host, you might need to replace 5001 with another value, such as 5002.

### Check the log output of the container

`$ docker container logs [container id]`
`* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)`
`172.17.0.1 - - [28/Jun/2017 19:35:33] "GET / HTTP/1.1" 200 -`

### Navigate to http://localhost:5001 in a browser to see the results.

You should see "hello world!" in your browser.
