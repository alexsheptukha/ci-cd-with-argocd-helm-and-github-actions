""" Тестирование приложения """
import unittest
import json
from app import app
class TestApp(unittest.TestCase):
    """
    Тест приложения
    """
    def setUp(self):
        """
        Настройка тестового клиента
        """
        self.app = app.test_client()
    def test_get_tasks(self):
        """
        Проверка получения всех задач
        """
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
    def test_add_task(self):
        """
        Проверка добавления задачи
        """
        response = self.app.post('/tasks', json={
            'title': 'Test task',
            'description': 'Test description'
            })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.get_data()), {
            'id': 1,
            'title': 'Test task',
            'description': 'Test description'
            })
            
if __name__ == '__main__':
    unittest.main()
