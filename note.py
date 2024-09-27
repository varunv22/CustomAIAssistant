from langchain_core.tools import tool

def note_tool(note):
    """
    Appends a text note to a local file called 'notes.txt'.

    Args:
        note (str): The text note to be saved.
    """
    with open("notes.txt", "a") as f:
        f.write(note + "\n")