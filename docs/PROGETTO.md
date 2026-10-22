# Task Manager — Specifiche del laboratorio

## Funzioni attuali
- Creazione task con titolo e assegnatario
- Completamento ed eliminazione per ID
- Ricerca testuale e filtro per stato
- Riepilogo aggregato

## Evoluzioni possibili (NON implementate)
- Livelli di priorità e filtro per priorità
- Ordinamento dei task
- Validazione degli assegnatari
- Gestione scadenze
- Report suddiviso per persona
- Formattazione avanzata dell'output

## Situazioni collaborative da simulare
- Due sviluppatori modificano funzioni distinte
- Due sviluppatori modificano lo stesso punto in questo documento o nel modello `Task`
- Un branch evolve mentre un altro resta indietro
- Un commit deve essere riportato su un altro branch tramite cherry-pick
- Una feature dipende da un'altra prima che la prima venga integrata in `main`

**Nota:** le modifiche conflittuali e i branch divergenti vanno prodotti dagli studenti durante il laboratorio; la baseline deve restare stabile e testabile.
