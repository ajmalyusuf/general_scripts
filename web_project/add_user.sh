if [ $# -gt 0 ]
then
    username=$1
else
    username='aaa'
fi

make_admin='False'
if [ "$username" == "admin" ] || [ "$username" == "ajmal" ]
then
    make_admin='True'
fi

echo "from app.models import User" > user.dat
echo "from app import db" >> user.dat
echo "user=User(email='$username@myweb.com',username='$username',password='$username',is_admin=$make_admin,first_name='$username',last_name='$username')" >> user.dat
echo "db.session.add(user)" >> user.dat
echo "db.session.commit()" >> user.dat

export FLASK_CONFIG=development
export FLASK_APP=run.py
flask shell < user.dat
