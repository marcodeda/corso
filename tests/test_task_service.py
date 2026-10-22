import unittest

from app.models.task import Task
from app.task_service import aggiungi_task, completa_task, elimina_task
from app.task_filter import cerca_per_titolo, filtra_per_stato
from app.task_report import riepilogo


class TaskManagerTest(unittest.TestCase):
    def setUp(self):
        self.tasks = [Task(1, "Scrivere documentazione", False, "Anna")]

    def test_aggiungi_task(self):
        nuovo = aggiungi_task(self.tasks, "Scrivere test", "Marco")
        self.assertEqual(nuovo.id, 2)
        self.assertEqual(len(self.tasks), 2)

    def test_rifiuta_titolo_vuoto(self):
        with self.assertRaises(ValueError):
            aggiungi_task(self.tasks, "   ")

    def test_completa_task(self):
        self.assertTrue(completa_task(self.tasks, 1))
        self.assertTrue(self.tasks[0].completato)
        self.assertFalse(completa_task(self.tasks, 99))

    def test_elimina_task(self):
        self.assertTrue(elimina_task(self.tasks, 1))
        self.assertEqual(self.tasks, [])
        self.assertFalse(elimina_task(self.tasks, 99))

    def test_filtri(self):
        aggiungi_task(self.tasks, "Test automatici")
        self.assertEqual(len(cerca_per_titolo(self.tasks, "TEST")), 1)
        self.assertEqual(len(filtra_per_stato(self.tasks, False)), 2)

    def test_report(self):
        self.assertEqual(riepilogo(self.tasks), "Task totali: 1 | Completati: 0 | Aperti: 1")


if __name__ == "__main__":
    unittest.main()
