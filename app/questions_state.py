from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Question(StatesGroup):
    feel_now = State()
    want_to_feel = State()
    able_to_do = State()
