# Task Manager — Laboratorio Git e GitHub, Giorno 2

Piccola applicazione Python **senza dipendenze esterne**, predisposta per esercizi su collaborazione, branch, merge, rebase, cherry-pick e dipendenze fra feature.

## Avvio

Richiede Python 3.10 o superiore.

```bash
python -m app.main
python -m unittest discover -s tests -v
```

## Struttura
- `app/models/task.py`: modello Task
- `app/task_service.py`: gestione dei task
- `app/task_filter.py`: funzioni di ricerca
- `app/task_report.py`: report testuale
- `app/main.py`: esempio eseguibile
- `tests/`: test automatici
- `docs/PROGETTO.md`: requisiti e possibili evoluzioni

## Uso nel Giorno 2
Un solo repository remoto, **cloni locali separati** per gli sviluppatori. Partire sempre da `main` aggiornato, creare feature branch e verificare le modifiche in VS Code / Git Graph.

La baseline è volutamente semplice: **non** contiene ancora priorità strutturate, filtri per priorità, ordinamento per scadenza e gestione avanzata degli stati. Queste funzionalità sono materiale per le esercitazioni.

Per prove di merge/rebase indipendenti creare branch `lab/...` separati; non forzare push su branch condivisi. Il docente decide quando pubblicare le modifiche e quando aprire Pull Request.

Il Modulo 6 su monorepo, multirepo e submodules è escluso da questo repository.
