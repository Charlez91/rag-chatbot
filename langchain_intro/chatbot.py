import dotenv
from langchain_openai import ChatOpenAI
from langchain.schema.messages import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate

dotenv.load_dotenv()

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

messages = [
    SystemMessage(
        content="""You're an assistant knowledgeable about
            healthcare. Only answer healthcare-related questions."""
    ),
    HumanMessage(
        content="What is Medicaid Managed Care?"
    ),
]

chat_model.invoke(messages)#it answers what is parsed in as content for the humanmessages and behaves as described by systemmessage

#if a message not related to healthcare is asked it will not answer but tell you it only answers/provides assistance on healthcare related questions
messages = [
    SystemMessage(
        content="""You're an assistant knowledgeable about
            healthcare. Only answer healthcare-related questions."""
    ),
    HumanMessage(
        content="How do I change a tire?"
    ),
]

ans = chat_model.invoke(messages)#it will reply that it cant answer