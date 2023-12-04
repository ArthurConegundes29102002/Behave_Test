from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#------------------------------------------------------- configs do selenium:

# Selenium_Service = Service(ChromeDriverManager().install())
Navigator = webdriver.Chrome()
homepage_url = 'http://localhost:5000'

#-------------------------------------------------------

#abrir a paǵina principal
Navigator.get('http://localhost:5000')

#checar se o título da página corresponde
@given(u'i am on the homepage')
def step_impl(context):
    homepage_title= WebDriverWait(Navigator,3).until(EC.presence_of_element_located((By.ID, 'page_title')))
    assert homepage_title is not None, "o usuário não foi direcionado para a página principal"


# Aguardar até que o elemento com ID 'table_title' seja visível na página
@then(u'the table title should be present')
def step_impl(context):
    table_title = WebDriverWait(Navigator, 3).until(EC.presence_of_element_located((By.ID, 'table_title')))
    assert table_title is not None, "título da tabela não está presente na página"


#a primeira row da tabela está presente
@then('the first table row should be present')
def step_impl(context):
    first_row = WebDriverWait(Navigator,3).until(EC.presence_of_element_located((By.ID, 'titles_row')))
    assert first_row is not None


#a caixa de texto está presente
@then('the input box should be present')
def step_impl(context):
    input_box = WebDriverWait(Navigator,3).until(EC.presence_of_element_located((By.ID, 'content_box')))
    assert input_box is not None, "caixa de texto não está presente na página"


#o botão de adicionar task está presente
@then('the Add Task button should be present')
def step_impl(context):
    button = WebDriverWait(Navigator,3).until(EC.presence_of_element_located((By.ID, 'add_task_button')))
    assert button is not None, "botão não está presente na página "


