from nicegui import ui

START_HASH = 0x9E3779B1
MULTIPLIER = 0x517CC1C7
MASK = 0xFFFFFFFF 

def twist_hash(text: str) -> int:
    h = START_HASH

    for char in text:
        char_code = ord(char)
        
        h = h ^ char_code
        
        h = h * MULTIPLIER
        
        h = h & MASK
        
    h = h ^ len(text)
    
    final_hash = h & MASK
    
    return final_hash


def calculate_and_display_hash():
    message = input_text.value
    result = twist_hash(message)
    hash_result.set_text(f'Hash value: {result}')

#layout
with ui.card().classes('w-full max-w-lg'):  
    ui.label('Hashing').style("color: red; font-size: 50px")
    ui.add_css('.q-field--labeled .q-field__label { red ; font-weight: bold; }')

    input_text = ui.input(label='Enter Message', value='Hi', placeholder='Type your message here')
    hash_result = ui.label('Hash value: 2912524232')

    input_text.classes('w-full').props('outlined')

    with ui.row().classes('items-center'):
        hash_result.classes('text-lg font-bold text-red-800 bg-red-200 p-1 rounded')

    ui.button('GET HASH', color = "red", on_click=calculate_and_display_hash).classes()
    
calculate_and_display_hash() 

ui.run(title = 'Hashing')