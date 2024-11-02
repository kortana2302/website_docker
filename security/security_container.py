import json
import requests

class SecurityContainer:
  def __init__(self, security_service_url, api_key):
    self.security_service_url = security_service_url
    self.api_key = api_key

  def check_access(self, request_data):
    headers = {'Authorization': f'Bearer {self.api_key}'}
    response = requests.post(
      f'{self.security_service_url}/check_access',
      headers=headers,
      json=request_data
    )
    if response.status_code == 200:
      return response.json()['is_allowed']
    else:
      return False

  def handle_intrusion(self, intrusion_data):
    headers = {'Authorization': f'Bearer {self.api_key}'}
    response = requests.post(
      f'{self.security_service_url}/handle_intrusion',
      headers=headers,
      json=intrusion_data
    )
    if response.status_code != 200:
      print(f'Ошибка при отправке данных о вторжении: {response.status_code}')

  def get_security_recommendations(self):
    headers = {'Authorization': f'Bearer {self.api_key}'}
    response = requests.get(
      f'{self.security_service_url}/recommendations',
      headers=headers
    )
    if response.status_code == 200:
      return response.json()
    else:
      return {}

# Пример использования 
if __name__ == '__main__':
  security_service_url = 'http://security-service:8080'
  api_key = '12345'
  security_container = SecurityContainer(security_service_url, api_key)

  # Проверка доступа
  request_data = {'user_id': 123, 'resource_id': 456}
  if security_container.check_access(request_data):
    print('Доступ разрешен')
  else:
    print('Доступ запрещен')

  # Обработка вторжения
  intrusion_data = {'intrusion_type': 'unauthorized_access', 'source_ip': '192.168.1.1'}
  security_container.handle_intrusion(intrusion_data)

  # Получение рекомендаций по безопасности
  recommendations = security_container.get_security_recommendations()
  print(recommendations)
