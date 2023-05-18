from functions import alternate_caps
import PySimpleGUI as sg

label1 = sg.Text('Enter a word/sentence: ')
input_box = sg.Input(key = 'input')
output_label = sg.Text(key = 'output')
convert_button = sg.Button('Convert')

window = sg.Window('Alternating Capitalization',
                   layout = [[label1, input_box],
                             [convert_button],[output_label]], font = ('Helvetica', 11))


while True:
    event, values = window.read()
    print('EVENT',event)
    print('VALUES',values)

    text_to_convert = values['input']
    converted_text = alternate_caps(text_to_convert)
    window['output'].update(value = f'{converted_text}')

window.close()











