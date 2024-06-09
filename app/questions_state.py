from aiogram.fsm.state import State, StatesGroup


class THE_ASKER(StatesGroup):
    feel_now = State()
    want_to_feel = State()
    able_to_do = State()
