- Clone the repo
- make sure python3 version is being used
- execute **_pip3 install flask_**
- execute **_python3 app.py_** to run the server
- (we can query the server with either localhost address or ip address of the host where the script is being executed from)
- Following are some of the example queries
1. http://127.0.0.1:5000/query?limit=5
2. http://127.0.0.1:5000/query?date=2012-06-04
3. http://127.0.0.1:5000/query?weather=rain
4. http://127.0.0.1:5000/query?weather=rain&limit=5
- execute **_python3 test-app.py_** to run the test script.

## Docker setup
### Steps for creating a Docker conatiner for api server
- #Create a network
- **_docker network create my-app-network_**
- **_cd docker-app_**
- #Build the image-
- **_docker build -t web-app ._**
- #run the container from the above image
- **_docker run -d -p 5000:5000 --name web-app --network my-app-network web-app_**
- Here the image is named web-app and it is binded to host port 5000, so that it is accessible from outside the container.
- check if the app is accessible from host by executing any query from the host's browser for example-
- http://127.0.0.1:5000/query?date=2012-06-04

### Steps for creating a Docker conatiner and running a test script in it-
- **_cd docker-test-app_**
- #Build the image-
- **_docker build -t test-app ._**
- #run the container from the above image
- **_docker run -network my-app-network test-app_**
- The container will run and execute the test script and should output the results on the console.
