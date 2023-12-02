import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

class SistemaStreaming:
    def __init__(self):
        self.usuarios = {"marcelo": "123", "felipe": "321"}
        self.perfis = {"marcelo": {"favoritos": []}, "felipe": {"favoritos": []}}
        self.catalogo = {"Filmes": ["Ilha do Medo", "O Show de Truman", "O Sexto Sentido", "O Lobo de Wallstreet", "Psicopata Americano"],
                         "Séries": ["Suits", "Round 6", "The Boys", "Stranger Things", "La Casa de Papel"]}

    def fazer_login(self):
        usuario = simpledialog.askstring("Login UNIFLIX LITE", "Digite o nome de usuário:")
        senha = simpledialog.askstring("Login UNIFLIX LITE", "Digite a senha:", show='*')
        return usuario if usuario in self.usuarios and self.usuarios[usuario] == senha else None

    def acessar_perfil(self, usuario):
        root = tk.Tk()
        root.title(f"Bem-vindo, {usuario}!")
        root.geometry("400x300")

        # Personaliza a cor de fundo
        root.configure(bg="#E50914")

        # Cria a fonte padrão do sistema para títulos em negrito
        fonte_titulo = ("Helvetica", 16, "bold")
        fonte_montserrat = ("Helvetica", 12)

        estilo = ttk.Style()
        estilo.configure("TButton", font=fonte_montserrat)

        # Adiciona um Label para exibir as opções
        label = tk.Label(root, text="UNIFLIX LITE", bg="#E50914", fg="white", font=fonte_titulo)
        label.pack(pady=10)

        # Adiciona botões para cada opção
        button_favoritos = ttk.Button(root, text="1. Lista de Favoritos", command=lambda: self.exibir_favoritos(usuario), style="TButton")
        button_catalogo_filmes = ttk.Button(root, text="2. Catálogo de Filmes", command=lambda: self.exibir_catalogo("Filmes"), style="TButton")
        button_catalogo_series = ttk.Button(root, text="3. Catálogo de Séries", command=lambda: self.exibir_catalogo("Séries"), style="TButton")
        button_adicionar_favorito = ttk.Button(root, text="4. Adicionar Filme aos Favoritos", command=lambda: self.adicionar_favorito(usuario), style="TButton")

        button_favoritos.pack(pady=5)
        button_catalogo_filmes.pack(pady=5)
        button_catalogo_series.pack(pady=5)
        button_adicionar_favorito.pack(pady=5)

        root.mainloop()

    def exibir_favoritos(self, usuario):
        perfil = self.perfis[usuario]
        messagebox.showinfo("Lista de Favoritos", f"Lista de Favoritos de {usuario}:\n{perfil['favoritos']}")

    def exibir_catalogo(self, tipo):
        catalogo = self.catalogo[tipo]
        catalogo_text = "\n".join(catalogo)
        messagebox.showinfo(f"Catálogo de {tipo}", f"Catálogo de {tipo}:\n{catalogo_text}")

    def adicionar_favorito(self, usuario):
        filme_escolhido = simpledialog.askstring("Adicionar Filme aos Favoritos", "Digite o nome do filme:")
        if filme_escolhido in self.catalogo["Filmes"]:
            perfil = self.perfis[usuario]
            perfil['favoritos'].append(filme_escolhido)
            messagebox.showinfo("Adicionado aos Favoritos", f"{filme_escolhido} foi adicionado aos favoritos.")
        else:
            messagebox.showerror("Erro", "Filme não encontrado no catálogo.")

    def menu_usuario(self, usuario):
        while True:
            print("\nBem-vindo à UNIFLIX LITE,", usuario + "!")
            print("1. Acessar Perfil*")
            print("2. Adicionar novo Perfil")
            print("3. Remover Perfil")
            print("4. Alterar Senha")
            print("5. Alterar Plano")
            print("0. Sair")
            escolha_usuario = input("Escolha uma opção: ")

            if escolha_usuario == "1":
                self.acessar_perfil(usuario)
            elif escolha_usuario == "0":
                break
            else:
                print("Opção inválida.")

def main():
    sistema = SistemaStreaming()

    while True:
        usuario_logado = sistema.fazer_login()

        if usuario_logado:
            sistema.menu_usuario(usuario_logado)
        else:
            print("Login falhou. Verifique seu nome de usuário e senha.")
            break

if __name__ == "__main__":
    main()