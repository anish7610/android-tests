### Test Setup

- Install Appium and uiautomator2 driver for android

    - npm install -g appium appium-doctor
    - appium doctor
    - appium driver install uiautomator2

- Create virtualenv and install dependencies

    - python3 -m venv myenv
    - source myenv/bin/activate
    - pip3 install -r requirements.txt

- Follow steps to setup the flask server here - https://github.com/anpa6841/flask-bank-backend

- Follow App setup here: https://github.com/anpa6841/bank-app/

- Start Appium Server: appium --log-level debug

- Run tests: pytest -v

### [Test Execution](https://github.com/user-attachments/assets/64e78f4b-e55a-4849-8e63-b07b90c451d5)


