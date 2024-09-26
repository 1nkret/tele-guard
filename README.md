# TeleGuard: Telegram Blocker & PC Control Bot

TeleGuard — это программа, которая помогает защитить ваш компьютер, 
автоматически блокируя доступ к Telegram при его запуске. Программа 
также включает бота для удаленного управления компьютером, который 
предоставляет множество полезных функций.

## Особенности
- **FOR WINDOWS ONLY**
- **Автоматическая блокировка Telegram**:
  - Программа отслеживает запуск Telegram и автоматически закрывает его, если не введена определенная комбинация клавиш.
- **Удаленное управление через бота**:
  - Получайте уведомление о запуске компьютера.
  - Выключайте компьютер через бота.
  - Запускайте консольные команды для пранка пользователя.
  - Выводите изображение с веб-камеры на полный экран.
  - Отправляйте фотографию на полный экран.
  - Закройте все приложения на вашем компьютере с помощью 1 кнопки.
  - Заблокируйте курсор пользователю.
  - Диспетчер задач в вашем телефоне
  - Можно дать доступ своему другу
  - Режим не беспокоить (отключить возможность вашим друзьям управлять компьютером)

## Как это работает
1. При старте компьютера запускается программа, которая также активирует бота.
2. Вы получаете уведомление через бота о том, что компьютер запущен.
3. Telegram закрывается, если пользователь не вводит правильную комбинацию клавиш.
4. Через бота вы можете управлять компьютером удаленно.

## Установка 

1. Клонируйте репозиторий:
```bash
git clone https://github.com/1nkret/tele-guard.git
```

2. Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте dot-env файл с вашими параметрами:
```env
API_TOKEN='your-bot-token'
OWNER='your_telegram.chat.id'
ALLOWED_CHAT_IDS='your_friends.chat.id','your_girlfriend.chat.id','and_more.chat.id'
BLOCKER='false'
```
**OWNER** - владелец может быть всего один, но в самом боте можно добавить совладельца.
**BLOCKER** - если установить 'true', то у вас будет включена функция блокировки
Telegram Desktop (для разблокировки, при открытии консоли нажмите 3 раза на ESC)

4. Создайте в планировщике задач новую задачу ![img](https://i.imgur.com/WtFLCUq.png)

5. Добавьте триггер ![img](https://i.imgur.com/sLhZlUp.png)

6. Теперь нужно добавить сам скрипт в эту задачу. Создайте "Действие", после чего пропишите в
"Программа или сценарий" путь к вашему интерпретатеру (path/to/project/.venv/Scripts/pythonw.exe 
(pythonw.exe - для фоновой работы)). Далее в "Добавить аргументы" прописываем путь к main.py
(path/to/project/main.py). В последней строке прописываем путь к проекту и нажимаем "ОК".
![img](https://i.imgur.com/vSiaj2C.png)

7. После нажатия "ОК", мы добавили нашу программу в планировщик задач. Теперь после запуска 
компьютера, бот будет запускаться автоматически.

## Запуск
1. Запустите программу
```bash
python main.py
```

2. Теперь вы можете пользоваться ботом.

## Команды
- `/menu` - меню
- `/help` - руководство


*Only better from here on out... 1nkret <3*
