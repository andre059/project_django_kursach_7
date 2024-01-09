
python3 -m vene env
source env/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
deactivate