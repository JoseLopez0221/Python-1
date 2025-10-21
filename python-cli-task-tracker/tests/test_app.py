import os
import json
import unittest
from pathlib import Path
import app

class TestTaskTracker(unittest.TestCase):
    def setUp(self):
        # Isolate test data file
        self.data = Path("tasks.json")
        if self.data.exists():
            self.data.unlink()

    def tearDown(self):
        if self.data.exists():
            self.data.unlink()

    def test_add_and_list(self):
        app.add_task("Test item")
        tasks = json.loads(self.data.read_text())
        self.assertEqual(len(tasks), 1)
        self.assertFalse(tasks[0]["done"])
        self.assertEqual(tasks[0]["title"], "Test item")

if __name__ == "__main__":
    unittest.main()