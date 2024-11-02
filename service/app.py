import json
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Симулированные данные для демонстрации 
users = {
  123: {'role': 'admin'},
  456: {'role': 'user'}
}
resources = {
  456: {'owner': 123}
}

@app.route('/check_access', methods=['POST'])
def check_access():
  data = request.get_json()
  user_id = data.get('user_id')
  resource_id = data.get('resource_id')

  if user_id in users and resource_id in resources:
    if users[user_id]['role'] == 'admin' or users[user_id]['role'] == 'user' and users[user_id]['id'] == resources[resource_id]['owner']:
      return jsonify({'is_allowed': True})
    else:
      return jsonify({'is_allowed': False})
  else:
    return jsonify({'is_allowed': False})

@app.route('/handle_intrusion', methods=['POST'])
def handle_intrusion():
  data = request.get_json()
  # Обработка вторжения, например, запись в лог
  print(f"Вторжение обнаружено: {data}")
  return jsonify({'success': True})

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
  recommendations = {
    'recommendation1': 'Обновите пароли',
    'recommendation2': 'Включите двухфакторную аутентификацию'
  }
  return jsonify(recommendations)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
