# Imports
import tkinter as tk
from tkinter import ttk, filedialog
import qrcode
from PIL import Image, ImageTk
import io

# Configurações visuais
COR_PRINCIPAL = "#6366f1"
COR_BG_GRADIENTE = "#e0e7ff"
COR_CARD = "#fff"
COR_TEXTO = "#222"
COR_DICA = COR_PRINCIPAL
COR_BORDA = COR_PRINCIPAL
TAMANHO_CARD = 220
TAMANHO_QR = 180

# Função para gerar o QR Code
def gerar_qrcode():
    texto = entrada_texto.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    qr.add_data(texto)
    qr.make(fit=True)
    img = qr.make_image(fill_color=COR_TEXTO, back_color=COR_CARD)
    img = img.resize((TAMANHO_QR, TAMANHO_QR))
    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format="PNG")
    img_byte_array = img_byte_array.getvalue()
    img_bytes = Image.open(io.BytesIO(img_byte_array))
    qr_image = ImageTk.PhotoImage(img_bytes)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Arquivos PNG", "*.png")])
    if file_path:
        with open(file_path, 'wb') as f:
            f.write(img_byte_array)
        status_label.config(text="✔ QR salvo com sucesso!", foreground=COR_PRINCIPAL)
    else:
        status_label.config(text="")

# Função principal da interface
def main():
    global entrada_texto, qr_label, status_label
    janela = tk.Tk()
    janela.title("✨ Gerador de QR Code ✨")
    janela.geometry("500x650")
    janela.configure(bg=COR_BG_GRADIENTE)

    # Gradiente fake usando um frame colorido
    bg_top = tk.Frame(janela, bg=COR_PRINCIPAL, height=180)
    bg_top.pack(fill='x', side='top')

    # Estilo visual
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', foreground="#fff", background=COR_PRINCIPAL, font=('Segoe UI', 14, 'bold'), padding=12, borderwidth=0)
    style.map('TButton', background=[('active', '#4338ca')])
    style.configure('TLabel', background=COR_BG_GRADIENTE, font=('Segoe UI', 12))
    style.configure('TEntry', font=('Segoe UI', 13), relief='flat')

    # Frame principal centralizado
    main_frame = tk.Frame(janela, bg="#f8fafc", bd=0, highlightbackground=COR_BORDA, highlightthickness=2)
    main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=520)

    # Título
    SUGESTAO_MINIMA = "🔗 Gere QR para links, textos ou contatos."
    titulo_label = tk.Label(main_frame, text="Gerador de QR Code", font=('Segoe UI', 22, 'bold'), bg="#f8fafc", fg=COR_PRINCIPAL)
    titulo_label.pack(pady=(32,8))
    info_label = tk.Label(main_frame, text=SUGESTAO_MINIMA, font=('Segoe UI', 11), bg="#f8fafc", fg=COR_DICA)
    info_label.pack(pady=(0,18))

    # Entrada de texto
    entrada_texto = tk.Entry(main_frame, font=('Segoe UI', 13), width=28, relief='flat', bg=COR_BG_GRADIENTE, fg=COR_TEXTO, highlightthickness=1, highlightbackground=COR_PRINCIPAL)
    entrada_texto.pack(pady=8, ipady=6)

    # Botão
    botao_gerar = tk.Button(main_frame, text="🚀 Gerar QR", command=gerar_qrcode, font=('Segoe UI', 14, 'bold'), bg=COR_PRINCIPAL, fg="#fff", activebackground="#4338ca", activeforeground="#fff", relief='flat', bd=0, padx=18, pady=8)
    botao_gerar.pack(pady=18)

    # Card do QR
    qr_card = tk.Frame(main_frame, bg=COR_CARD, bd=0, highlightbackground=COR_BORDA, highlightthickness=2, width=TAMANHO_CARD, height=TAMANHO_CARD)
    qr_card.pack(pady=18)
    qr_card.pack_propagate(False)
    qr_label = tk.Label(qr_card, bg=COR_CARD)
    qr_label.pack(padx=10, pady=10)

    # Status
    status_label = tk.Label(main_frame, text="", font=('Segoe UI', 12, 'bold'), bg="#f8fafc", fg=COR_PRINCIPAL)
    status_label.pack(pady=10)

    # Rodapé
    footer = tk.Label(janela, text="Feito com ❤️ por Sergio Andrade", font=('Segoe UI', 10), bg=COR_BG_GRADIENTE, fg=COR_PRINCIPAL)
    footer.pack(side='bottom', pady=12)

    janela.mainloop()

# Execução principal
if __name__ == "__main__":
    main()
