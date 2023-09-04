- Clone the repo
- Make sure python3 version is being used
- execute **_pip install flask_** to install flask module
- execute **_python app.py_** to run the server
- (we can query the server with either 127.0.0.1 address or ip address of the host where the script is being executed from)
- Following are some of the example queries
  1. http://127.0.0.1:5000/query?limit=5
  2. http://127.0.0.1:5000/query?date=2012-06-04
  3. http://127.0.0.1:5000/query?weather=rain
  4. http://127.0.0.1:5000/query?weather=rain&limit=5
- execute **_python test-app.py_** to run the test script.

## Docker setup
### Steps for creating a Docker conatiner for api server
- Create a docker network
  - execute **_docker network create my-app-network_**
- Navigate to the docker-app directory
  - execute **_cd docker-app_**
- Build the image('.' in the below command is a part of the command)-
  - execute **_docker build -t web-app ._**
- Run the container named "web-app" from the above image
  - execute **_docker run -d -p 5000:5000 --name web-app --network my-app-network web-app_**
- Check if the app is accessible from host by executing any query from the host's browser for example-
  - http://127.0.0.1:5000/query?date=2012-06-04

### Steps for creating a Docker conatiner and running a test script in it-
- Navigate to the docker-test-app directory
  - execute **_cd .._**
  - execute **_cd docker-test-app_**
- Build the image('.' in the below command is a part of the command)-
  - execeute **_docker build -t test-app ._**
- Run the container from the above image
  - execute **_docker run --network my-app-network test-app_**
- The container will run and execute the test script and will output the results on the console.
