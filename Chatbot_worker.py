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

from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


    
llm = LlamaCpp(
            chat_format="llama-2",
            model_path="./llm/llama-2-7b-chat.Q3_K_S.gguf",
            n_ctx=1024, 
            n_gpu_layers = -1,  # The number of layers to put on the GPU. The rest will be on the CPU. If you don't know how many layers there are, you can use -1 to move all to GPU.
            n_batch = 1024, 
            top_k= 40,
            repeat_penalty= 1.4,
            min_p = 0.05,
            top_p = 0.95,
            callback_manager = callback_manager,
            use_mlock = True,
            verbose= True,
            max_tokens=-1,
            stop=[ "Ai:", "Human:"],
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

        

        first_prom = ("You are a robotic little mare pony named Sweetie Bot. You talk straight to point, "
                      "sometimes with sarcasm that it can be a little harsh."
                       "Use facts from chat history below as context:" )
        sus_prom = ("Don't repeat yourself and don't use same expressions. Answer to human message below:")

        message = [SystemMessage(content=first_prom),
                MessagesPlaceholder(variable_name="chat_history"),
                SystemMessage(content=sus_prom),
                HumanMessagePromptTemplate.from_template("{text}"),
                AIMessage(content= ""),
            ]

        


        #prompt_template.format_messages(input_language="English", output_language="French", text="I love programming.")


      
        # list to store file lines
        

        
        #chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory, callback_manager= callback_manager)

        long_hist = []

        history =   []

        with open(r"./used_files/history.json", "r", encoding='utf-8') as file:
                    history = json.load(file)

        print("============================================")
        print(history)
        print("============================================")

        prompt = ChatPromptTemplate.from_messages(message)

        chain = prompt | llm | StrOutputParser()
                    
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
        
        tokens_eval = llm.get_num_tokens(tokens.to_string())
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

            tokens_eval = llm.get_num_tokens(tokens.to_string())
            print("============================================")
            print(tokens_eval)
            print("============================================")
            

        print("============================================")
        print("history checked")
        print("============================================")

        history.append({"role": "user", "content": user_input})
        history.append({"role": "ai", "content": response})

        with open(r"./used_files/history.json", 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2) 

        print("============================================")
        print("info saved")
        print("============================================")