# Progress so far

## Frontend:

Not started yet

## Backend:

Main.py - Created a simple health endpoint route with root() function that returns the message "This is agent breif app"

## Agent:

Agent.py - Setup a simple Langraph graph , first initialized the gpt-4o mini via init_chat_model. Defined an AssistantState(TypedDict) that contains a list of messages , then I made an assistant_node that takes the messages state and invokes the model and resturns the response as a syaye update

Finally I built the graph by adding assistant node as the start and end edge , then we compile the graph and finally test it by invoking the graph with a Human messaging "Hello who are you" and by printing out the latest response in messages[-1] we show the response
