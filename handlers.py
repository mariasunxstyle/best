# Здесь будет логика управления: шаги, позиции, переходы, таймеры, кнопки

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Кнопки управления — для шага
control_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
control_keyboard.add(KeyboardButton("⏭️ Пропустить"))
control_keyboard.add(KeyboardButton("⛔ Завершить"))
control_keyboard.add(KeyboardButton("↩️ Назад на 2 шага"))
control_keyboard.add(KeyboardButton("📋 Вернуться к шагам"))

# Кнопки после завершения шага (в один ряд)
complete_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
complete_keyboard.add(
    KeyboardButton("▶️ Продолжить"),
    KeyboardButton("📋 Вернуться к шагам"),
    KeyboardButton("↩️ Назад на 2 шага"),
    KeyboardButton("⛔ Завершить")
)

# Меню шагов (пример — будет динамически генерироваться)
steps_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
steps_keyboard.add(
    KeyboardButton("Шаг 1 (8 мин)"), KeyboardButton("Шаг 2 (9 мин)"), KeyboardButton("Шаг 3 (12 мин)")
)
steps_keyboard.add(
    KeyboardButton("Шаг 4 (20 мин)"), KeyboardButton("Шаг 5 (27 мин)"), KeyboardButton("Шаг 6 (38 мин)")
)
steps_keyboard.add(
    KeyboardButton("Шаг 7 (48 мин)"), KeyboardButton("Шаг 8 (60 мин)"), KeyboardButton("Шаг 9 (85 мин)")
)
steps_keyboard.add(
    KeyboardButton("Шаг 10 (110 мин)"), KeyboardButton("Шаг 11 (150 мин)"), KeyboardButton("Шаг 12 (190 мин)")
)
steps_keyboard.add(
    KeyboardButton("ℹ️ Инфо")
)

# Приветствие и инфо (вызываются в main.py)
GREETING = """Привет, солнце! ☀️
Ты в таймере по методу суперкомпенсации.
Кожа адаптируется к солнцу постепенно — и загар становится ровным, глубоким и без ожогов.

Начинай с шага 1. Даже если уже немного загорел(а), важно пройти путь с начала.
Каждый новый день и после перерыва — возвращайся на 2 шага назад.

Хочешь разобраться подробнее — жми /info. Там всё по делу."""

INFO_TEXT = """ℹ️ Инфо
Метод суперкомпенсации — это безопасный, пошаговый подход к загару.
Он помогает коже адаптироваться к солнцу, снижая риск ожогов и пятен.

Рекомендуем загорать с 7:00 до 11:00 и после 17:00 — в это время солнце мягкое,
и при отсутствии противопоказаний можно загорать без SPF.

Так кожа включает свою естественную защиту: вырабатывается меланин и гормоны адаптации.

С 11:00 до 17:00 — солнце более агрессивное. Если остаёшься на улице —
надевай одежду, головной убор или используй SPF.

Каждый новый день и после перерыва — возвращайся на 2 шага назад.
Это нужно, чтобы кожа не перегружалась и постепенно усиливала защиту.

Если есть вопросы — пиши: @sunxbeach_director"""
