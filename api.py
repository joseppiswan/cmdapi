from flask import Flask
import os
app = Flask('app')
@app.route('/hi', methods=['GET', 'POST'])
def hello_world():
  os.system('cmd /k "calc"')
  return 'Hello, World!'

app.run(host='0.0.0.0', port=105)