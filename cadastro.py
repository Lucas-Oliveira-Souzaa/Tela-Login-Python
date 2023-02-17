from PySimpleGUI import PySimpleGUI as sg

sg.theme('Black')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario',size=(30,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*',
    size=(30,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Primeira Tela de Login', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'lucas' and valores ['senha'] == '123456':
            print('Seja bem vindo, a minha primeira tela de login com Python!')
        else:
            print('Você digitou os dados incorreto. Tente novamente.')    