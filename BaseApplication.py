import PySimpleGUI as sg


def check_user(username):
    print(username)

def start_view():
    sg.theme('Dark')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Enter your email'), sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    username = ''
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        if event == 'Ok':
            username = values[0] = values[0].strip()
            check_user(username)

    window.close()


if __name__ == '__main__':
    start_view()
