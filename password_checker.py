import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Lista de contraseñas comunes
common_passwords = ["123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "password1"]

def check_password_strength(password):
    score = 0
    length = len(password)
    
    # Verifica la presencia de diferentes tipos de caracteres
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~" for char in password):
        score += 1
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    return score

def evaluate_password():
    password = password_entry.get()
    score = check_password_strength(password)
    
    # Comprueba si la contraseña está en la lista de contraseñas comunes
    if password in common_passwords:
        score = 0
        messagebox.showwarning("Contraseña Común", "Esta contraseña es demasiado común y no es segura.")

    # Evalúa la fortaleza de la contraseña basada en la puntuación
    if score <= 2:
        strength = "Muy débil"
        color = 'red'
    elif score == 3:
        strength = "Débil"
        color = 'orange'
    elif score == 4:
        strength = "Moderada"
        color = 'yellow'
    elif score == 5:
        strength = "Fuerte"
        color = 'lightgreen'
    elif score == 6:
        strength = "Muy fuerte"
        color = 'green'

    # Actualiza la barra de progreso personalizada
    progress_label.config(width=score * 20, bg=color)

    # Muestra el resultado
    messagebox.showinfo("Fortaleza de la Contraseña", f"La fortaleza de la contraseña es: {strength}")

    # Muestra sugerencias
    suggestions = []
    if score < 6:
        if len(password) < 12:
            suggestions.append("Haz la contraseña más larga.")
        if not any(char.isdigit() for char in password):
            suggestions.append("Añade algunos números.")
        if not any(char.islower() for char in password):
            suggestions.append("Añade algunas letras minúsculas.")
        if not any(char.isupper() for char in password):
            suggestions.append("Añade algunas letras mayúsculas.")
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~" for char in password):
            suggestions.append("Añade algunos caracteres especiales.")
        if password in common_passwords:
            suggestions.append("No uses contraseñas comunes.")
        suggestion_text.set("\n".join(suggestions))
    else:
        suggestion_text.set("¡Contraseña fuerte!")

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Muestra la contraseña generada en el campo de entrada de solo lectura
    generated_password_entry.config(state='normal')
    generated_password_entry.delete(0, tk.END)
    generated_password_entry.insert(0, password)
    generated_password_entry.config(state='readonly')
    

def on_password_entry_change(*args):
    password = password_var.get()
    score = check_password_strength(password)
    
    # Evalúa la fortaleza de la contraseña basada en la puntuación
    if score <= 2:
        strength = "Muy débil"
        color = 'red'
    elif score == 3:
        strength = "Débil"
        color = 'orange'
    elif score == 4:
        strength = "Moderada"
        color = 'yellow'
    elif score == 5:
        strength = "Fuerte"
        color = 'lightgreen'
    elif score == 6:
        strength = "Muy fuerte"
        color = 'green'

    # Actualiza la barra de progreso personalizada
    progress_label.config(width=score * 20, bg=color)

    # Muestra sugerencias
    suggestions = []
    if score < 6:
        if len(password) < 12:
            suggestions.append("Haz la contraseña más larga.")
        if not any(char.isdigit() for char in password):
            suggestions.append("Añade algunos números.")
        if not any(char.islower() for char in password):
            suggestions.append("Añade algunas letras minúsculas.")
        if not any(char.isupper() for char in password):
            suggestions.append("Añade algunas letras mayúsculas.")
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~" for char in password):
            suggestions.append("Añade algunos caracteres especiales.")
        if password in common_passwords:
            suggestions.append("No uses contraseñas comunes.")
        suggestion_text.set("\n".join(suggestions))
    else:
        suggestion_text.set("¡Contraseña fuerte!")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Verificador de Fortaleza de Contraseña")

# Ajusta el tamaño inicial de la ventana
root.geometry("800x800")

# Variable para el campo de entrada de la contraseña
password_var = tk.StringVar()
password_var.trace_add('write', on_password_entry_change)

# Etiqueta y entrada para la contraseña
ttk.Label(root, text="Ingrese su contraseña:").pack(pady=10)
password_entry = ttk.Entry(root, show='*', textvariable=password_var)
password_entry.pack(pady=10)

# Barra de progreso personalizada para la fortaleza de la contraseña
progress_label = tk.Label(root, text='', bg='grey', width=0, height=2)
progress_label.pack(pady=10)

# Botón para evaluar la fortaleza de la contraseña
evaluate_button = ttk.Button(root, text="Evaluar Contraseña", command=evaluate_password)
evaluate_button.pack(pady=10)

# Botón para generar una contraseña fuerte
generate_button = ttk.Button(root, text="Generar Contraseña Fuerte", command=generate_password)
generate_button.pack(pady=10)

# Entrada de solo lectura para mostrar la contraseña generada
ttk.Label(root, text="Contraseña Generada:").pack(pady=10)
generated_password_entry = ttk.Entry(root, state='readonly')
generated_password_entry.pack(pady=10)

# Etiqueta para mostrar sugerencias
suggestion_text = tk.StringVar()
suggestion_label = ttk.Label(root, textvariable=suggestion_text)
suggestion_label.pack(pady=10)

# Ejecuta el loop principal de la interfaz gráfica
root.mainloop()















