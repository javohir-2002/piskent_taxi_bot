from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderData(StatesGroup):
    name = State()
    from_where = State()
    to_where = State()
    num_of_people = State()
    price = State()
    phone = State()
    addition = State()
