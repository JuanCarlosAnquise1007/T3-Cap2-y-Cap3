import tkinter as tk
from tkinter import messagebox

# Función para ordenar una lista de enteros con la simulación de la máquina de Turing
def turing_sort(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambiar
                steps.append(list(arr))  # Guardar paso
    return arr, steps

# Función para ejecutar la ordenación cuando se hace clic en el botón
def execute_sort():
    input_numbers = entry.get()
    
    try:
        arr = [int(x) for x in input_numbers.split(",")]
        if all(0 <= x <= 100 for x in arr):
            sorted_arr, steps = turing_sort(arr)
            
            # Mostrar el proceso de ordenación en la caja de texto
            text_box.delete(1.0, tk.END)  # Limpiar el cuadro de texto
            text_box.insert(tk.END, "Proceso de ordenación paso a paso:\n")
            for idx, step in enumerate(steps):
                text_box.insert(tk.END, f"Paso {idx + 1}: {step}\n")
            
            text_box.insert(tk.END, "\nResultado final:\n")
            text_box.insert(tk.END, str(sorted_arr))
        else:
            messagebox.showerror("Error", "Introduce solo enteros entre 0 y 100.")
    except ValueError:
        messagebox.showerror("Error", "Introduce una lista válida de enteros separados por comas.")

# Crear la ventana principal
root = tk.Tk()
root.title("Máquina de Turing - Ordenación de Enteros")

# Crear los widgets de la interfaz
label = tk.Label(root, text="Introduce una lista de enteros separados por comas (0-100):")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

sort_button = tk.Button(root, text="Ordenar", command=execute_sort)
sort_button.pack(pady=10)

text_box = tk.Text(root, height=15, width=50)
text_box.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
