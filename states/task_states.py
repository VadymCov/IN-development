from aiogram.fsm.state import State, StatesGroup

class TaskStates(StatesGroup): # Condition for FSM
    waiting_for_task = State()
    waiting_for_id = State()