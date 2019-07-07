. ../env/bin/activate
cd ../app/
pip install -r requirements/prod.txt  | grep -v 'Requirement already satisfied' | grep -v 'Cleaning up...'
./manage.py migrate -v 0
./manage.py collectstatic --no-input
circusctl restart worker
