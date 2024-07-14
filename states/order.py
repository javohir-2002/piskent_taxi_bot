from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderData(StatesGroup):
    from_where = State()
    to_where = State()
    price = State()
    phone = State()
    status = State()


class Order(StatesGroup):
    phone = State()
    order_message = State()
    status = State()
