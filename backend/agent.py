from langchain.chat_models import init_chat_model
from typing import TypedDict
from dotenv import load_dotenv
load_dotenv()


model = init_chat_model(
  "gpt-4o-mini",
   temperature = 0 
)

#initial assistant state 

class AssistantState(TypedDict):
  messages: list

#initial assistant node

def assistant_node(state: AssistantState):
  """simple llm assistant"""

  messages = state["messages"]
  response = model.invoke(messages)

  return{
    "messages":[response]
  }





