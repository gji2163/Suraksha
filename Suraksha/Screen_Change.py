import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('SysLock.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://remote-f2ce1-default-rtdb.firebaseio.com/'
    }
)

def stream(message):
    print('\t',message.data[1].split()[0],'\n',message.data[1].split()[1],'\t',message.data[0])
    
ref = db.reference('/SysLock/Lenovo/Curr/').listen(stream)
