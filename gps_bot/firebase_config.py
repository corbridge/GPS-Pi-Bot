import pyrebase

def firebaseInit():
  firebaseConfig = {
  "apiKey": "AIzaSyCndLrX1QvxSug-lwX5-LfV1pTs_IegH3s",
  "authDomain": "gps-pi-bot.firebaseapp.com",
  "databaseaURL": "https://gps-pi-bot-default-rtdb.firebaseio.com",
  "projectId": "gps-pi-bot",
  "storageBucket": "gps-pi-bot.appspot.com",
  "messagingSenderId": "237945598717",
  "appId": "1:237945598717:web:3143f5d47f0f8a8fb84494"
  }

  firebase = pyrebase.initialize_app(firebaseConfig)
  db = firebase.database()

  return db