import tkinter as tk

def cerrar(event):
    root.destroy()

class ButtonMatrix:
    def __init__(self, root):
        self.root = root
        self.states = {
            "14_new": False, "14_as_good_as_new": False, "14_good": False,
            "15_new": False, "15_as_good_as_new": False, "15_good": False,
            "16_new": False, "16_as_good_as_new": False, "16_good": False,
            "17_new": False, "17_as_good_as_new": False, "17_good": False
        }
        self.columns = ['14', '15', '16', '17']
        self.rows = ['new', 'as_good_as_new', 'good']

        for i, row_label in enumerate(self.rows):
            tk.Label(root, text=row_label).grid(row=i+1, column=0)
        for j, col_label in enumerate(self.columns):
            tk.Label(root, text=col_label).grid(row=0, column=j+1)
        for i, row_label in enumerate(self.rows):
            for j, col_label in enumerate(self.columns):
                var_name = f"{col_label}_{row_label}"
                button = tk.Button(root, text="", width=10, height=2, bg="gray",
                                   command=lambda v=var_name: self.toggle_button(v))
                button.grid(row=i+1, column=j+1)
        self.show_states_button = tk.Button(root, text="Mostrar Estados", command=self.show_states)
        self.show_states_button.grid(row=len(self.rows)+1, column=0, columnspan=len(self.columns)+1)

    def toggle_button(self, var_name):
        current_state = self.states[var_name]
        self.states[var_name] = not current_state
        button = self.get_button(var_name)
        button.config(bg="green" if self.states[var_name] else "gray")

    def get_button(self, var_name):
        col_label, row_label = var_name.split('_', 1)
        col_index = self.columns.index(col_label) + 1
        row_index = self.rows.index(row_label) + 1
        return self.root.grid_slaves(row=row_index, column=col_index)[0]

    def show_states(self, event=None):
        for key, value in self.states.items():
            print(f"{key}: {'Seleccionado' if value else 'No seleccionado'}")

root = tk.Tk()
root.title("Matriz de Botones")
button_matrix = ButtonMatrix(root)
root.bind('<q>', button_matrix.show_states)
root.bind('<Escape>', cerrar)
root.mainloop()