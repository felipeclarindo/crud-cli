from ..modules.exceptions import ValidateError


def validate_table(table: str):
    try:
        table = table.strip()
        if table:
            if table.isalnum() or "_" in table:
                return True
            else:
                raise ValidateError("Não é aceito caracteres especiais.")
        else:
            raise ValidateError("A tabela não pode estar vazia.")
    except ValidateError as e:
        print(f"Error: {e}")
    return False


def validate_column(column: str) -> bool:
    try:
        column = column.strip()
        if column:
            if column.isalnum():
                return True
            else:
                raise ValidateError("A coluna não conter caracteres especiais.")
        else:
            raise ValidateError("A coluna não pode estar vazia.")
    except ValidateError as e:
        print(f"Error: {e}")
    return False


def validate_value(value: str) -> bool:
    try:
        value = value.strip().replace(" ", "")
        if value:
            if value.isalnum():
                return True
            else:
                raise ValidateError("O valor não pode conter caracteres especiais")
        else:
            raise ValidateError("O valor não pode estar vazio.")
    except ValidateError as e:
        print(f"Error: {e}")
    return False


def validate_id(id: str, id_list: list[id]) -> bool:
    try:
        if id:
            if id.isdigit() and id != None:
                if int(id) in id_list:
                    return True
                else:
                    raise ValidateError("Id não encontrado.")
            else:
                raise ValidateError("O Id deve conter apenas números.")
        else:
            raise ValidateError("O id não pode estar vazio.")
    except ValidateError as e:
        print(f"Error: {e}")
    return False
