# FSM (Finite State Machine) позволяет боту запоминать, на каком этапе диалога находится пользователь.
# Без FSM бот забывает предыдущую фразу сразу после ответа. С FSM он понимает
# “Сейчас я жду от пользователя именно название города, а не что-то другое”.

# 1. Создание состояний
# Состояния описываются как класс, наследуемый от StatesGroup. Каждое состояние - это объект State().

from aiogram.fsm.state import StatesGroup, State

class WeatherStates(StatesGroup):
    waiting_for_city = State()
    confirming_details = State()


# 2. Запуск состояния (Переход)
# Чтобы бот начал ждать данные, нужно установить состояние для конкретного пользователя.

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Привет! Введи название своего города:")
    await state.set_state(WeatherStates.waiting_for_city)


# 3. Обработка сообщения в состоянии (Фильтр)
# Теперь хендлер будет реагировать на текст только тогда, когда пользователь находится в нужном статусе.


@router.message(WeatherStates.waiting_for_city)
async def process_city(message: Message, state: FSMContext):
    city = message.text
    # Здесь логика запроса к API погоды

    await message.answer(f"В городе {city} отличная погода!")
    # Сбрасываем состояние, чтобы бот перестал ждать город
    await state.clear()