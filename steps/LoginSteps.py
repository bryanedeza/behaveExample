from behave import Given, When, Then
from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage

class LoginSteps:

    @Given("Que estamos en la pantalla del login")
    def verify_login_page(context):
        context.login_page_object = LoginPage(context.web_driver)
        context.login_page_object.verify_login_page()

    @When("Haya ingresado mi usuario y contraseña y presionando entrar")
    def send_user_password(context):
        context.login_page_object.send_user_password("standard_user", "secret_sauce")
        context.login_page_object.press_login_button()

    @Then("Valida que mi sesion este activa")
    def verify_active_session(context):
        context.product_list_page_object = ProductListPage(context.web_driver)
        context.product_list_page_object.verify_product_list_page()

