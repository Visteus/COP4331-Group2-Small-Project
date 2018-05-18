# Contact Manager Project - Group 2 
Contact Manager: Oracle DB, Python/Django, JavaScript. 

Credit: Harrison, Jacob, Tom, David, Jesus, Terrel, Tuan
## Installation Guide (Mac OS + Linux)
1. Clone project from github (git clone)
2. Install pip (pip: a package manager) 
 * ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```
 * ```sudo python get-pip.py```
3. Install virtualenv (development environment)
 * ```pip install virtualenv```
4. Change directory to project's directory
5. ```virtualenv env -p python3```
6. ```source env/bin/activate```
7. ```pip install -r requirements.txt```
8. ```cd contactmanager```
9. ```python manage.py migrate```
10. To run the app: ```python manage.py runserver```