class UsuarioPrototype:
    def __init__(self):
        self.idade = 18
        self.nome = "Visitante"
        self.tipo_acesso = "Padrão"
        self.limite_download = "10GB"
        self.email = None

    def clone(self):
        return UsuarioPrototype()
