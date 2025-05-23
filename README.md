## Telegram-бот Tracking Task Bot

---
Телеграм бот [API-сервиса для постановки и отслеживания задач](https://github.com/AlexeyDemidow/tracking_tasks_project)

Сервис позволяет:
- Получать список ваших задач
- Отслеживать дедлайны
- Получать уведомления

Команды:
- Команда /start — приветствие
- Команда /mytasks — возвращает список активных задач из API для telegram_user_id, равного message.from_user.id
- Команда /done <task_id> — помечает задачу как выполненную

### Установка и запуск

- Клонируйте репозиторий
- Установите зависимости `pip install -r requirements.txt`
- Создаем `.env` файл по образцу в `.env.example`
- Убедиться что [основной сервис](https://github.com/AlexeyDemidow/tracking_tasks_project) запущен
- После запуска основного сервиса в Docker или локально выполните `python bot.py`

