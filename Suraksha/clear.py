import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('SysLock.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://remote-f2ce1-default-rtdb.firebaseio.com/'
    }
)

ref = db.reference('/SysLock/Dell/')

data = ref.get()

ref.set({
    'Curr'  :   data['Curr'],
    'Mode'  :   data['Mode'],
    'vid'   :   data['vid']
    }
)

data.pop('Curr')
data.pop('Mode')
data.pop('vid')

d = ''
with open('logs.txt', 'a') as f:
    for i in data:
        d += i + '\t' + data[i] + '\n'
    f.write(d) 
    f.close()

#for i,j in ref.get().items():
 #   print(i,'\t',j)
