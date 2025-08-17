# PlantCare Telegram Bot (Python + aiogram)

Це каркас бота для догляду за кімнатними рослинами:
- Python + aiogram (webhook через FastAPI)
- База: Postgres (Neon)
- Деплой: Render (Free)
- Крон: Render Jobs → POST `/scheduler`

## Швидкий старт (локально)
1. Створи та заповни `.env` на основі `.env.example`.
2. Встанови залежності:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Ініціалізуй БД (через Neon SQL Editor) скриптом `scripts/init_db.sql`.
4. Запусти:
   ```bash
   uvicorn app.main:app --reload
   ```

Далі слідуй інструкції в чаті 😉
