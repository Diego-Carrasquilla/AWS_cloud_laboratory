from fastapi import FastAPI
import os

app = FastAPI(title="SimpleHelloAPI")

@app.get("/hello")
def read_root(name: str = "Mundo"):
        ambiente = os.getenv("AMBIENTE_DESPLIEGUE", "Local")
        ascii_art = r"""
            _   _       _ _          _   _      _ _ _         
         | | | | ___ | | | ___    | | | | ___| | | | ___    
         | |_| |/ _ \| | |/ _ \   | |_| |/ _ \ | | |/ _ \   
         |  _  | (_) | | |  __/   |  _  |  __/ | | |  __/   
         |_| |_|\___/|_|_|\___|   |_| |_|\___|_|_|_|\___|   
        """
        saludo = f"Hola, {name}!\nSaludos desde la arquitectura Serverless en ambiente: {ambiente}.\nDesarrollado por Diego Carrasquilla y Andres Jaramillo.\n\n{ascii_art}"
        return {"message": saludo}
