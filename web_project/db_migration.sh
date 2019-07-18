export FLASK_CONFIG=development
export FLASK_APP=run.py

# To create a migration repository (one time)
# This creates a migrations directory and contents

flask db init

flask db migrate
flask db upgrade

echo "Check database using:"
echo "mysql -u root"
