from aiogram.fsm.state import State, StatesGroup

class WordStates(StatesGroup): # Condition for FSM
    waiting_for_word = State()
    waiting_for_id = State()