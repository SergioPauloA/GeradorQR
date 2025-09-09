import tkinter as tk

from tkinter import ttk, filedialog

import qrcode

from PIL import Image, ImageTk

import io




# Função para gerar o QR Code

def gerar_qrcode():

    # Obtém o texto da entrada de texto

    texto = entrada_texto.get()

    # Cria um objeto QRCode

    qr = qrcode.QRCode(

        version=1,

        error_correction=qrcode.constants.ERROR_CORRECT_L,

        box_size=5,  # menor para garantir espaço

        border=2,

    )

   

    # Adiciona o texto ao QRCode

    qr.add_data(texto)

    qr.make(fit=True)

    # Cria uma imagem do QRCode

    img = qr.make_image(fill_color="#222", back_color="#fff")

    img = img.resize((180, 180))  # menor que o card

    # Converte a imagem em um formato de bytes

    img_byte_array = io.BytesIO()

    img.save(img_byte_array, format="PNG")

    img_byte_array = img_byte_array.getvalue()

    # Cria uma imagem PhotoImage a partir dos bytes

    img_bytes = Image.open(io.BytesIO(img_byte_array))

    qr_image = ImageTk.PhotoImage(img_bytes)

    # Exibe a imagem em uma etiqueta

    qr_label.config(image=qr_image)

    qr_label.image = qr_image

    # Salva a imagem como um arquivo PNG

    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])

    if file_path:

        with open(file_path, 'wb') as f:

            f.write(img_byte_array)

        status_label.config(text="✔ QR salvo com sucesso!", foreground="#0078d7")

    else:

        status_label.config(text="")


# Cria a janela principal com gradiente
janela = tk.Tk()
janela.title("✨ Gerador de QR Code ✨")
janela.geometry("500x650")
janela.configure(bg="#e0e7ff")

# Gradiente fake usando um frame colorido
bg_top = tk.Frame(janela, bg="#6366f1", height=180)
bg_top.pack(fill='x', side='top')

# Estilo vislumbrante
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', foreground="#fff", background="#6366f1", font=('Segoe UI', 14, 'bold'), padding=12, borderwidth=0)
style.map('TButton', background=[('active', '#4338ca')])
style.configure('TLabel', background="#e0e7ff", font=('Segoe UI', 12))
style.configure('TEntry', font=('Segoe UI', 13), relief='flat')

# Frame principal centralizado com sombra
main_frame = tk.Frame(janela, bg="#f8fafc", bd=0, highlightbackground="#6366f1", highlightthickness=2)
main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=520)

# Título vislumbrante
SUGESTAO_MINIMA = "🔗 Gere QR para links, textos ou contatos."
titulo_label = tk.Label(main_frame, text="Gerador de QR Code", font=('Segoe UI', 22, 'bold'), bg="#f8fafc", fg="#6366f1")
titulo_label.pack(pady=(32,8))

# Dica curta com emoji
info_label = tk.Label(main_frame, text=SUGESTAO_MINIMA, font=('Segoe UI', 11), bg="#f8fafc", fg="#6366f1")
info_label.pack(pady=(0,18))

# Entrada de texto estilizada
entrada_texto = tk.Entry(main_frame, font=('Segoe UI', 13), width=28, relief='flat', bg="#e0e7ff", fg="#222", highlightthickness=1, highlightbackground="#6366f1")
entrada_texto.pack(pady=8, ipady=6)

# Botão animado
botao_gerar = tk.Button(main_frame, text="🚀 Gerar QR", command=gerar_qrcode, font=('Segoe UI', 14, 'bold'), bg="#6366f1", fg="#fff", activebackground="#4338ca", activeforeground="#fff", relief='flat', bd=0, padx=18, pady=8)
botao_gerar.pack(pady=18)

# Card do QR com sombra e borda colorida
qr_card = tk.Frame(main_frame, bg="#fff", bd=0, highlightbackground="#6366f1", highlightthickness=2, width=220, height=220)
qr_card.pack(pady=18)
qr_card.pack_propagate(False)
qr_label = tk.Label(qr_card, bg="#fff")
qr_label.pack(padx=10, pady=10)

# Status com animação e ícone
status_label = tk.Label(main_frame, text="", font=('Segoe UI', 12, 'bold'), bg="#f8fafc", fg="#6366f1")
status_label.pack(pady=10)

# Rodapé elegante
footer = tk.Label(janela, text="Feito com ❤️ por Sergio Andrade", font=('Segoe UI', 10), bg="#e0e7ff", fg="#6366f1")
footer.pack(side='bottom', pady=12)

# Inicia o loop da interface gráfica
janela.mainloop()