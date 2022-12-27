# A simple Python Flask API to generate password

### <ins>Steps to setup the project<ins>:

1. Create a project directory flask_password_api (any other name is also fine).

2. Move to directory created in above step.

3. Issue `git clone https://github.com/s4hms/flask-password-api`
   (if git is not installed download the repo in ZIP format using "Code" button and extract files into directory created in steps 1)

4. Move to cloned/extracted directory and create a virtual environment and activate it. For more details on how to create and activate virtual environment, watch here [Windows](https://www.youtube.com/watch?v=APOPm01BVrk) and [MAC/LINUX](https://www.youtube.com/watch?v=Kg1Yvry_Ydk) accordingly.

5. Install the required package by issuing `pip install -r requirements.txt` in the above virtual environment.

**If you're not used to working with virtual environments then you can install the Flask package to your default Python interpreter by issuing `pip install Flask`**

6. Run the python script by issuing `python app.py`.

API documentation can be accessed at `http://localhost:5000/` once the project is deployed.

API end points have be attached after `http://localhost:5000/generate?`.

**Example**: `http://localhost:5000/generate?uc=2&lc=8`
