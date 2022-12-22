Feature: Login

  Scenario: Validar inicio de sesion correcto
    Given Que estamos en la pantalla del login
    When Haya ingresado mi usuario y contraseña y presionando entrar
    Then Valida que mi sesion este activa