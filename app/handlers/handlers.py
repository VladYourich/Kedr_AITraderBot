from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, CommandObject

from config.config import HELP, START
import app.keyboards as kb
router = Router()


# Обработчики команд -----------------------------------------------------------------
@router.message(CommandStart())     #deep_link=True, magic=F.args.isdigit()
async def cmd_start(message: Message, command: CommandObject):
    await message.answer(START, reply_markup=kb.main)
    #await message.answer(f'Привет! Ты пришел от {command.args}')
    
@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(HELP)
    await message.answer(f"Твой ID: {message.from_user.id} \nТвой username: {message.from_user.username}")

# Обработчики объектов -----------------------------------------------------------------
@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фотографии: {message.photo[-1].file_id}')

@router.message()
async def other_cmd(message: Message):
    await message.answer('Чой-то я не пОняла... А шо это было?')