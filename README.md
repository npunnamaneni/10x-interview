clone the repo
make sure python3 version is being used
execute "pip3 install flask"
execute "python3 app.py" to run the server
(we can query the server with either localhost address or ip address of the host where the script is being executed from)
Following are some of the example queries-
1. http://127.0.0.1/query?limit=5
2. http://127.0.0.1/query?date=2012-06-04
3. http://127.0.0.1/query?weather=rain
4. http://127.0.0.1/query?weather=rain&limit=5
execute "python3 test-app.py" to run the test script.

Docker setup
Steps for creating a Docker conatiner for api server
#Create a network
docker network create my-app-network
cd docker-app
#Build the image-
docker build -t web-app .
#run the container from the above image
docker run -d -p 5000:5000 -name web-app -network my-app-network web-app
Here the image is named web-app and it is binded to host port 5000, so that it is accessible from outside the container.
check if the app is accessible from host by executing any query from the host's browser for example-
http://127.0.0.1/query?date=2012-06-04

Steps for creating a Docker conatiner and running a test script in it-
cd docker-test-app
#Build the image-
docker build -t test-app .
#run the container from the above image
docker run -network my-app-network test-app
The container will run and execute the test script and should output the results on the console.
