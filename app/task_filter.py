from app.models.task import Task


def filtra_per_stato(tasks: list[Task], completato: bool) -> list[Task]:
    return [task for task in tasks if task.completato == completato]


def cerca_per_titolo(tasks: list[Task], testo: str) -> list[Task]:
    testo = testo.casefold()
    return [task for task in tasks if testo in task.titolo.casefold()]
