from nicegui import ui
from random import shuffle

BASE_EMOJIS = ['🪼', '☎️', '💛', '🌀', '🌼', '🦞', '🦋', '🛵'] 
EMOJIS = BASE_EMOJIS * 2
shuffle(EMOJIS)

buttons = []
opened = []  
matched = [] 
game_locked = False 

def reset_pair():
    global game_locked
    
    if len(opened) == 2:
        i, j = opened[0], opened[1]
        
        buttons[i].set_text('❓')
        buttons[j].set_text('❓')
        
        buttons[i].classes(remove='bg-amber-300')
        buttons[j].classes(remove='bg-amber-300')
        
        opened.clear()
        game_locked = False

def handle_click(idx: int):
    global game_locked
    
    if idx in matched or idx in opened or game_locked:
        return

    buttons[idx].set_text(EMOJIS[idx])
    buttons[idx].classes(add='bg-red-300')

    opened.append(idx)

    if len(opened) == 2:
        game_locked = True
        
        i, j = opened[0], opened[1]
        
        if EMOJIS[i] == EMOJIS[j]:
            matched.extend([i, j])
            buttons[i].classes(remove='bg-red-300', add='bg-red-400')
            buttons[j].classes(remove='bg-red-300', add='bg-red-400')
            opened.clear()
            game_locked = False
            
            if len(matched) == len(EMOJIS):
                ui.notify('🎉 You win! 🎉', type='positive', position='center', timeout=3000)

        else:
            ui.timer(0.5, reset_pair, once=True)

#layout    
ui.label('‼️ Memory Game ‼️').style("color: red; font-size: 50px")

#4x4 grid
ui.add_css('.extra-large-emoji { font-size: 50px; }')
with ui.grid(columns=4).classes('gap-1'):
    for i, emoji in enumerate(EMOJIS):
        btn = ui.button('❓', color = "red", on_click=lambda idx=i: handle_click(idx))
        btn.classes('w-30 h-30 text-3xl font-bold bg-red-500 hover:bg-red-600 extra-large-emoji')
        buttons.append(btn)
        
ui.run(title='Memory Game')