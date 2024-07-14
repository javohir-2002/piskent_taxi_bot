from aiogram.dispatcher.filters.state import StatesGroup, State


class OrderData(StatesGroup):
    # name = State()
    from_where = State()
    to_where = State()
    # num_of_people = State()
    price = State()
    phone = State()
    # addition = State()
    status = State()


class Order(StatesGroup):
    phone = State()
    order_message = State()
    status = State()
