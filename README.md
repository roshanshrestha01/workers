## Work Orders

Application to organizer worker and their assigned work order. Application contributes to properly manage
workers and their assign work orders

### Installation

Below are bash to be execute to fully run project in development environment. 

```bash
mkdir project
cd project
Copy project zip
Unzip project zip
virtualenv env
source env/bin/activate
cd app
pip install -r requirements/dev.txt
python manage.py migrate
python manage.py runserver
```
Server running at http://localhost:8000/

### Project

Application in deployed at https://demo.rktcnepal.com/

https://demo.rktcnepal.com/admin for admin access with:

Username: admin \
Password: admin123

### Necessary Endpoint

Development \
BASE_URL = http://localhost:8000/ 

Production \
BASE_URL = https://demo.rktcnepal.com/ 


####  Worker List

URL: BASE_URL + 'v1/workers/' \
Method: GET 

####  Worker Create

URL: BASE_URL + 'v1/workers/' \
Method: POST \
Data:
```json
{
  "name": "Name of worker",
  "company_name": "Name of company",
  "email": "Worker email"
}
``` 

####  Worker Delete

URL: BASE_URL + 'v1/workers/<workder_id>' \
Method: DELETE 


####  Fetch all Work Order List

URL: BASE_URL + 'v1/work-orders/' \
Method: GET

####  Sort all Work Order List with deadline

Ascending\
URL: BASE_URL + 'v1/work-orders/?ordering=deadline' \
Method: GET

Descending\
URL: BASE_URL + 'v1/work-orders/?ordering=-deadline' \
Method: GET 

####  Work Order Create

URL: BASE_URL + 'v1/work-orders/' \
Method: POST \
Data:
```json
{
  "title": "Work order title",
  "description": "Work order description",
  "deadline": "Deadline in YYYY-MM-DD format"
}
```

#### Assign work orders

URL: BASE_URL + 'v1/work-orders/<work_order_id>/assign/<worker_id>/' \
Method: GET

#### Unassign work orders

URL: BASE_URL + 'v1/work-orders/<work_order_id>/unassigned/<worker_id>/' \
Method: GET

#### Work orders specific to worker

URL: BASE_URL + 'v1/workers/<worker_id>/work_orders/' \
Method: GET
