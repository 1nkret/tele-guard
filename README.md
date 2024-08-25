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

## Как это работает
1. При старте компьютера запускается программа, которая также активирует бота.
2. Вы получаете уведомление через бота о том, что компьютер запущен.
3. Telegram закрывается, если пользователь не вводит правильную комбинацию клавиш.
4. Через бота вы можете управлять компьютером удаленно.

## Установка 

1. Клонируйте репозиторий:
```bash
git clone repo
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
```
**OWNER** - это люди с высшими правами доступа к вашему компьютеру 
(имеют все права к боту), а **ALLOWED_CHAT_IDS** - это те, кому вы можете 
доверять.


## Запуск
1. Запустите блокировку телеграмма:
```bash
python main.py
```

2. Запустите бота:
```bash
python Bot/telegram_bot.py
```

3. Теперь вы можете пользоваться ботом.

## Команды
- `/shutdown` - Выключить компьютер.
- `/prank` - Запустить консоль для пранка.
- `/takephoto` - Сделать фотографию с веб камеры
- `/uploadphoto` - Отобразить вашу фотографию на экране
- `/error` - Вызвать ошибку на экране


*Only better from here on out... 1nkret <3*