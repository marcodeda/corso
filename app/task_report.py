from app.models.task import Task


def riepilogo(tasks: list[Task]) -> str:
    """Restituisce un riepilogo testuale, senza stampare direttamente."""
    totali = len(tasks)
    completati = sum(task.completato for task in tasks)
    return f"Task totali: {totali} | Completati: {completati} | Aperti: {totali - completati}"
