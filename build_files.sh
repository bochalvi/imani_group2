echo "BUILD START"
python3.13.2 -m pip install -r requirements.txt
python3.13.2 manage.py collectstatic --noinput --clear
echo "BUILD END"