# Importar dependencias:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Definir agente:
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

# Función para enviar mensajes:
def send_message(NAME, PASSWORD, CHAT, MESSAGE):
  # Configurar Chrome:
  chrome_options = Options()
  chrome_options.add_argument('user-agent={0}'.format(user_agent))
  chrome_options.add_argument("--headless")

  # Abrir Chrome y navegar a Rocket:
  driver = webdriver.Chrome(options=chrome_options)
  driver.get("https://rocketchat.avature.net/")

  # Iniciar sesión:
  driver.implicitly_wait(10)
  input_user = driver.find_element(By.CLASS_NAME, "rcx-input-box--type-text")
  if input_user:
    input_user.send_keys(NAME)

  input_pass = driver.find_element(By.CLASS_NAME, "rcx-input-box--type-password")
  if input_pass:
    input_pass.send_keys(PASSWORD)

  button = driver.find_element(By.CLASS_NAME, "rcx-button--primary")
  if button:
    button.click()

  # Recorrer chats y seleccionar el elegido:
  driver.implicitly_wait(10)
  enlaces = driver.find_elements(By.CLASS_NAME, "rcx-sidebar-item--clickable")
  for enlace in enlaces:
    if enlace.text == CHAT:
      enlace.click()

  # Escribir y enviar mensaje:
  driver.implicitly_wait(10)
  input_message = driver.find_element(By.CLASS_NAME, "rc-message-box__textarea")
  input_message.send_keys(MESSAGE)
  input_message.send_keys(Keys.ENTER)

  # Terminar ejecución:
  driver.quit()