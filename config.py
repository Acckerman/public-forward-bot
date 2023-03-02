import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "18517936"))
    API_HASH = os.environ.get("API_HASH", "552ce63ba82ea7a633b039ee0dc87790")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5867827039:AAHaCU6Gp7lkAqM25p_FvM8V2ptlrk4Ptio")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1753576629")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Filestore:filestoreacc@cluster0.pcffnsj.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Filestore")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQBhmScTP9n3QR-eVEC58ZFugKOuNYkSaXZYRDI248mpSmT5wePJKZH7wpBNy7fi7JxB7Zc3lmDkXza-VteO1itFQ0b-voD2fViNt0APl8sWrDqnU11BKynD9c2Wqvfj0k8hL_IuZPqJsFqH5LUMOy0M2t5EPU6ECnLW-OEWyLMYPxOhftHFrxIF2XPVqqd0tGgAsN08QNdeQ-GTNXuHv5QmyZIjy-k_GiL8RPcMdnzLZIoaL8QAT2-6g78S0cvSk2KPy55Ihke0PAd5V5PddxvGAg5fE2r_Pz7FNakOW3gY9P30eTn-RVQMQ1WF3r-sE5_t8i7qbR1dfkC8W9q_7ymBaIV0tQA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
