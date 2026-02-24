from langchain_groq import ChatGroq 
from dotenv import load_dotenv

import os
import json
import uuid
import logging
from datetime import datetime



load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
#print("GROQ_API_KEY:", GROQ_API_KEY)
#Set LLM
models=["llama-3.3-70b-versatile","openai/gpt-oss-20b"]

groq_chat=ChatGroq(api_key=GROQ_API_KEY,model=models[0],temperature=0,disable_streaming=False)
#response=groq_chat.invoke([{"role":"user","content":"Write a poem about the love in ghanean pidging."}])
#print("Response:", response) 

def setup_logging():
    """Configure logging to save logs in JSON format"""
    logger=logging.getLogger("Chatbot")

    #Create a file handler for JSON logs
    file_handler=logging.FileHandler("chat_logs.json")
    formater=logging.Formatter('%(message)s')  # Log message as JSON
    file_handler.setFormatter(formater)
    logger.addHandler(file_handler)
    console_handler=logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    logger.addHandler(console_handler)
   

    return logger


def initialize_llm(model:str=models[0]) -> ChatGroq: 
    """Initialize the LLM and return the chat instance"""
    try:
        groq_chat=ChatGroq(api_key=GROQ_API_KEY,model=model,temperature=0,disable_streaming=False)
        print(groq_chat)
        return groq_chat
    except Exception as e:
        
        raise   

#initialize_llm()

class Chatbot:
    
    def __init__(self,model:str=models[0]):
        self.client=initialize_llm()
        self.logger=setup_logging()
        self.session_id=str(uuid.uuid4())
        self.user_id=str(uuid.uuid4())
        self.model_name=model
        
        self.messages=[{"role":"system","content":"You are a helpful assistant."}] # To store the conversation history

    
    def chat(self,user_input:str) -> str:
        try:
    
            log_entry={
                "timestamp": datetime.now().isoformat(),
                "level":"INFO",
                "type":"user_input",
                "metadata":{
                    "session_id": self.session_id,
                    "model": self.model_name,
                    "user_id": self.user_id
                }
                
            }
            self.logger.info(json.dumps(log_entry))
            #append user message 

            self.messages.append({"role":"user","content":user_input})

            #generate response from the model
            start_time=datetime.now()
            response=self.client.invoke(self.messages)
            end_time=datetime.now()
            
            #calculate response time
            response_time=(end_time-start_time).total_seconds()

            #extract response content
            response_content=response.content if response else "No response"
            
            #log model response and performance metrics
            log_entry={
                "timestamp": end_time.isoformat(),
                "level":"INFO",
                "type":"model_response",
                "model_response": response_content,
                

                }

            self.logger.info(json.dumps(log_entry))
            #append model response to messages
            self.messages.append({"role":"assistant","content":response_content})   
            return response_content
        except Exception as e:
            log_entry={
                        "timestamp": datetime.now().isoformat(),
                        "level":"ERROR",
                        "type":"chat_error",
                        "error_message": str(e),
                        "metadata":{
                            "session_id": self.session_id,
                            "model": self.model_name,
                            "user_id": self.user_id
                        }
                    }
            self.logger.error(json.dumps(log_entry))
            return "Sorry, an error occurred while processing your request."
        
        
def main():
    #model selection
    print("Available models:")
    for i, model in enumerate(models):
        print(f"{i+1}. {model}")
    model_choice=int(input("Select a model by number: "))
    print("\n ")
    chatbot=Chatbot()
    response=chatbot.chat("Write a poem about the love in ghanean pidgin.")
    print("Chatbot response:", response)

if __name__=="__main__":
    main()


    