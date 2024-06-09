from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.message import TextMessage
from app.questions_state import THE_ASKER

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(TextMessage.HELLO)


@router.message(Command('test'))
async def update_first(message: Message, state: FSMContext):
    await state.set_state(THE_ASKER.feel_now)
    await message.answer(TextMessage.FEEL_NOW)


@router.message(THE_ASKER.feel_now)
async def second_answer(message: Message, state: FSMContext):
    await state.update_data(fi=message.text)
    await state.set_state(THE_ASKER.want_to_feel)
    await message.answer(TextMessage.WANT_TO_FEEL)


@router.message(THE_ASKER.want_to_feel)
async def third_answer(message: Message, state: FSMContext):
    await state.update_data(sec=message.text)
    await state.set_state(THE_ASKER.able_to_do)
    await message.answer(TextMessage.ABLE_TO_DO)


@router.message(THE_ASKER.able_to_do)
async def done(message: Message, state: FSMContext):
    await state.update_data(tr=message.text)
    data = await state.get_data()
    await message.answer(f'Твои ответы:\n\n'
                         f'{TextMessage.FEEL_NOW}:\n{data["fi"]}\n\n'
                         f'{TextMessage.WANT_TO_FEEL}:\n{data["sec"]}\n\n'
                         f'{TextMessage.ABLE_TO_DO}:\n{data["tr"]}')


@router.message(Command('help'))
async def update_first(message: Message):
    await message.answer('Помощи тут пока нет :(')
