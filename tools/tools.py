from langchain_core.tools import tool


@tool
def save_on_file(filename: str, content: str) -> str:
    """
    Salva una stringa di testo in un file nel filesystem.
    Usa questo strumento ogni volta che l'utente chiede di scrivere, creare o salvare un documento in un file.
    Salva SEMPRE i file nella sottocartella 'output'.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"Successo: Il file '{filename}' è stato creato sul filesystem!"
    except Exception as e:
        return f"Errore durante il salvataggio: {e}"