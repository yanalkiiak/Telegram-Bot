
from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from openai import AsyncClient

import os

key = os.getenv("OPENROUTER_API_KEY")

router=Router()

async def generate_response(prompt):
    client = AsyncClient(
    base_url="https://openrouter.ai/api/v1",
    api_key=key,
    )

    completion = await client.chat.completions.create(
    extra_body={},
    model="google/gemma-3-27b-it:free",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )
    return completion.choices[0].message.content



@router.message(CommandStart())
async def cmd_start(message:    Message):
    await message.answer('Привіт! Я тобі допоможу з будь-яким питанням стосовно домашніх улюбленців')

@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.reply('Чим саме я вам можу допомогти?')

@router.message(F.text=='Допомога')
async def helpp(message:Message):
    await message.reply('Чим саме я вам можу допомогти?')

@router.message(F.text=='Завершити')
async def stopp(message:Message):
    await message.answer('Ви зупинили бота.')

@router.message(F.text=='Розпочати')
async def startt(message:Message):
    await message.answer('Привіт! Я тобі допоможу з будь-яким питанням стосовно домашніх улюбленців')

@router.message(F.text=='Контакти')
async def cont(message:Message):
    await message.answer('За додатковою інформацією можете звернутись на пошту helpanimal@gmail.com')

@router.message(Command('stop'))
async def cmd_stop(message: Message):
    await message.answer('Ви зупинили бота.')

@router.message()
async def cmd_ai(message:Message):
    msg=await message.answer('Зачекайте, бот перевертає догори дном весь інтернет в пошуках відповіді...')
    response = await generate_response(message.text)
    await msg.delete()
    await message.answer(f'{response}')



