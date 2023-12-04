from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#---------------------------------------------------------------

Navigator = webdriver.Chrome()
homepage_url = 'http://localhost:5000'

Navigator.get(homepage_url)

#---------------------------------------------------------------


#checar se o usuário está na homepage
@given(u'the user is on the home page')
def step_impl(context):
    homepage_title= WebDriverWait(Navigator,3).until(EC.presence_of_element_located((By.ID, 'page_title')))
    assert homepage_title is not None, "o usuário não foi direcionado para a página principal"

#checar quando usuário clicou no botão
@when(u'the user click the delete button')
def step_impl(context):
    pass

#checar se o elemento foi removido de fato
@Then(u'the element is removed from the DB')
def step_impl(context):
    pass
    #checar se o usuário foi redirecionado para a HPage
    #checar se a tabela foi atualizada