🌍 [Read in English](README.md)

# Crud

Crud para manipulações em banco de dados oracle com métodos de inserção, atualização, captura e remoção de dados. utilizando a biblioteca `requests` em python.

# Tecnologias Utilizadas

- `requests` - Comunicação com a api.
- `pytest` - Realizaçaõ dos testes.
- `oracledb` - Conectar com a database da oracle.
- `python-dotenv` - Carregar variaveis de ambientes.
- `flask` - Desenvolvimento da api.
- `flask_cors` - Configuração do CORS da api.

# Funcionalidades

- Manipulação de dados de uma database: Métodos de inserção, atualização, criação e remoção de dados utilizando requests.
- Interface simples e intuitiva: Interface em linha de comando simples e entuitiva para manipulação de um banco de dados.
- Dinamico: Interface dinamica, podendo manipular a tabela que desejar!

## Passos para instalação e execução

1. Clone o repositório:

```bash
git clone https://github.com/felipeclarindo/crud-cli.git
```

2. Entre no diretório:

```bash
cd crud-cli
```

3. Crie o `Ambiente Virtual`:

```bash
python -m venv .venv
```

4. Ative o `Ambiente Virtual` executando o arquivo `.bat` em `.venv/Scripts/activate.bat`.

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

6. Execute o servidor da api:

```bash
python src/api/server.py
```

7. Execute a aplicação:

```bash
python src/main.py
```

8. Interaja com a interface do menu e realize a manipulação desejada no banco de dados.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

Felipe Clarindo

- [LinkedIn](https://www.linkedin.com/in/felipe-clarindo-934578289/)
- [Instagram](https://www.instagram.com/lipethegoat)
- [GitHub](https://github.com/felipeclarindo)

## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
