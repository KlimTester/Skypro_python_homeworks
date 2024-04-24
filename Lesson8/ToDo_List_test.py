import requests

class ToDoClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_task(self, title):
        """Создание задачи."""
        url = f"{self.base_url}/tasks"
        response = requests.post(url, json={"title": title})
        return response.json()

    def rename_task(self, task_id, new_title):
        """Переименование задачи."""
        url = f"{self.base_url}/tasks/{task_id}"
        response = requests.put(url, json={"title": new_title})
        return response.json()

    def delete_task(self, task_id):
        """Удаление задачи."""
        url = f"{self.base_url}/tasks/{task_id}"
        response = requests.delete(url)
        return response.status_code

    def get_tasks(self):
        """Получение списка всех задач."""
        url = f"{self.base_url}/tasks"
        response = requests.get(url)
        return response.json()

    def get_task(self, task_id):
        """Получение конкретной задачи."""
        url = f"{self.base_url}/tasks/{task_id}"
        response = requests.get(url)
        return response.json()

    def mark_task_completed(self, task_id):
        """Отметить задачу как 'Выполнена'."""
        url = f"{self.base_url}/tasks/{task_id}"
        response = requests.put(url, json={"completed": True})
        return response.json()

    def unmark_task_completed(self, task_id):
        """Снять отметку 'Выполнена'."""
        url = f"{self.base_url}/tasks/{task_id}"
        response = requests.put(url, json={"completed": False})
        return response.json()

# Пример использования класса
if __name__ == "__main__":
    client = ToDoClient("https://sky-todo-list.herokuapp.com")
    print(client.create_task("Написать статью"))
    print(client.get_tasks())
    print(client.rename_task(1, "Обновить статью"))
    print(client.mark_task_completed(1))
    print(client.unmark_task_completed(1))
    print(client.delete_task(1))
