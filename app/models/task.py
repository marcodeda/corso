from dataclasses import dataclass


@dataclass
class Task:
    id: int
    titolo: str
    completato: bool = False
    assegnatario: str = ""
