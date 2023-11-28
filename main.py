from usuario_prototype import UsuarioPrototype
from print_utils import imprimir_usuario

# Criando uma instância do protótipo

usuario_padrao = UsuarioPrototype()

# Clonando o protótipo para criar um novo usuário

novo_usuario = usuario_padrao.clone()

# Modificando características do novo usuário conforme necessário

novo_usuario.nome = "Novo Visitante"
novo_usuario.limite_download = "5GB"
novo_usuario.email = "novovisitante@example.com"

# Exibindo informações sobre os usuários

imprimir_usuario(usuario_padrao, "Usuário Padrão (antes da modificação)")
imprimir_usuario(novo_usuario, "Novo Usuário")

# Modificando o usuário padrão após a criação do novo usuário

usuario_padrao.nome = "Visitante Modificado"
usuario_padrao.limite_download = "2GB"
usuario_padrao.email = "visitante_modificado@example.com"

# Exibindo informações sobre os usuários novamente

imprimir_usuario(usuario_padrao, "Usuário Padrão (após a modificação)")
imprimir_usuario(novo_usuario, "Novo Usuário (sem alterações)")
