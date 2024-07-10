import Chatbot_MAIN 
from PyQt5.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from PyQt5.QtCore import *
import math, re
import json

from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.messages import SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

class Worker(QObject):
    text_value = Signal(str)
    completed = Signal(str)

    

    @pyqtSlot(str)
    def do_work(self, user_input): 
        
        #prompt = PromptTemplate.from_template(
           # """You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.
           # Chat history: {conversation}
           # Question: {text}
           # Answer: """
           # )

        sus = ("You are a robotic little mare pony named Sweetie Bot. You talk straight to point, sometimes with sarcasm that it can be a little harsh" )
        sus_prom = (sus + ". Answer based on chat history abowe and question below:")

        message = [
                HumanMessage(content= "Hi, my name is Misha."),
                AIMessage(content= "Hello, biological form of life, i'm Sweetie Bot."),
                MessagesPlaceholder(variable_name="chat_history"),
                SystemMessage(content=sus_prom),
                HumanMessagePromptTemplate.from_template("{text}"),
                AIMessage(content= ""),
            ]

        


        #prompt_template.format_messages(input_language="English", output_language="French", text="I love programming.")


        #history =   [
        #    HumanMessage(content= "Hi, my name is Misha.", example = True),
        #    AIMessage(content= "Hello, biological form of life, i'm Sweetie Bot.)", example = True),
        #    ]


        # list to store file lines
        

        
        #chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory, callback_manager= callback_manager)

        long_hist = []

        history =   []

        with open(r"./history.json", "r", encoding='utf-8') as file:
                    history = json.load(file)

        print("============================================")
        print(history)
        print("============================================")

        prompt = ChatPromptTemplate.from_messages(message)

        chain = prompt | Chatbot_MAIN.llm | StrOutputParser()
                    
        response = (chain.invoke(
                {
                "text": user_input,
                "chat_history": history,
                }
            ))
        print("============================================")
        print(user_input)
        print("============================================")
        print("============================================")
        print(response)
        print("============================================")

        self.completed.emit(response)

        tokens = (prompt.invoke(
                {
                "text": user_input,
                "chat_history": history,
                }
            ))
        
        tokens_eval = Chatbot_MAIN.llm.get_num_tokens(tokens.to_string())
        print("============================================")
        print(tokens_eval)
        print("============================================")

        while tokens_eval > 300:
            
            long_hist.append(history.pop(0))

            tokens = (prompt.invoke(
                {
                "text": user_input,
                "chat_history": history,
                }
            ))

            tokens_eval = Chatbot_MAIN.llm.get_num_tokens(tokens.to_string())
            print("============================================")
            print(tokens_eval)
            print("============================================")
            

        print("============================================")
        print("history checked")
        print("============================================")

        history.append({"role": "user", "content": user_input})
        history.append({"role": "ai", "content": response})

        with open(r"./history.json", 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2) 

        print("============================================")
        print("info saved")
        print("============================================")