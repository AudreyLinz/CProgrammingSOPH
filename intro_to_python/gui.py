from nicegui import ui

ui.label('Welcome to nicegui').style("color: purple; font-size: 40px")

#create a greeting

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger >:)"}"
    ui.notify(msg) #create a popup

input_field = ui.input("Enter ur name: ")
ui.button("Greet Me!", color = "green", on_click = greet)

#Create a counter

class State:
    count = 0

    count_label = ui.label("Count: 0")

    def add_one():
        State.count += 1
        count_label.text = f"Count:{State.count}"

ui.button("Add one", color = "red", on_click =add_one)

ui.run(title="intro to nicegui")