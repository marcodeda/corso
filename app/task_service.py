from app.models.task import Task


def aggiungi_task(tasks: list[Task], titolo: str, assegnatario: str = "") -> Task:
    """Crea un task e lo aggiunge alla lista."""
    if not titolo.strip():
        raise ValueError("Il titolo non può essere vuoto")
    nuovo_id = max((task.id for task in tasks), default=0) + 1
    task = Task(id=nuovo_id, titolo=titolo.strip(), assegnatario=assegnatario)
    tasks.append(task)
    return task


def completa_task(tasks: list[Task], task_id: int) -> bool:
    """Segna un task come completato; False se non esiste."""
    for task in tasks:
        if task.id == task_id:
            task.completato = True
            return True
    return False


def elimina_task(tasks: list[Task], task_id: int) -> bool:
    """Elimina un task per ID; False se non esiste."""
    for indice, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[indice]
            return True
    return False
