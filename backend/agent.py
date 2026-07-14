from langchain.chat_models import init_chat_model
from typing import TypedDict
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage

load_dotenv()

#initialize the chat model client
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

#create the graph(add state)
graph_builder = StateGraph(AssistantState)

#Add nodes
graph_builder.add_node("assistant", assistant_node)

#define graph flow
graph_builder.add_edge(START, "assistant")
graph_builder.add_edge("assistant", END)

#compile the graph 
assistant_graph = graph_builder.compile()

#test the graph 
result = assistant_graph.invoke({
  "messages":[HumanMessage(content = "Hello, who are you")]
})

print(result["messages"][-1].content)






