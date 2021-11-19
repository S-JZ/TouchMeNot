 # TouchMeNot
![Touch Me Not](/0.jpg)

We have tried to develop a proof of concept for the following:
- Virtual Doodle
- Self Checkout
- Classroom


![V Doodle](/1.jpg)
_Virtual Doodle_
![Grocery Self Checkout](/2.jpg)
_Grocery Self Checkout_
## Virtual Doodle
The user needs to move his hand just like a wand of a magician, to transform his imagination into real artwork. The doodle can also be saved in thein doodle gallery afterward.
## Virtual Classroom
This tool offers touch-free navigation for teachers using common desktops to deliver lectures in the classroom.

## Self Checkout
The self-checkout provides a touch-free navigation and form-filling option using speech and gesture recognition.

### Tech Stack
- Python
- OpenCV
- Mediapipe
- Django
- HTML/CSS/BootStrap
- AutoPy
- Speech Recognition

### Dependencies
__Django__ 
``` sh
$ pip install django
```
__Speech Recognition__ 
```sh
$ pip install Speech Recognition
``` 
__MediaPipe__ 
``` sh
$ pip install mediapipe
```
__PyAudio__                  
``` sh
$ pip install PyAudio
```  
__Autopy__ 
```sh
$ pip install autopy
```
__OpenCV__ 
``` sh
$ pip install opencv-python
``` 

### How to Set Up?
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/S-JZ/TouchMeNot.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd TouchMeNot
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Youtube Demo Link:
https://www.youtube.com/watch?v=1h2ujLJPU1Q

## References:

1. https://docs.djangoproject.com/en/3.2/

2. https://pypi.org/project/autopy/

3. https://mediapipe.dev/

4. https://docs.opencv.org/4.x/

5. https://getbootstrap.com/

6. https://github.com/ravigithub19/ai-virtual-mouse

