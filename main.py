from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configuración de la conexión a la base de datos
engine = create_engine('mysql+pymysql://usuario:contraseña@localhost/nombre_de_la_base_de_datos')
Session = sessionmaker(bind=engine)

# Declaración del modelo de datos
Base = declarative_base()

class Palabra(Base):
    __tablename__ = 'palabras'

    id = Column(Integer, primary_key=True)
    palabra = Column(String(50), unique=True)
    significado = Column(String(200))

# Funciones para interactuar con la base de datos

def agregar_palabra(palabra, significado):
    session = Session()
    nueva_palabra = Palabra(palabra=palabra, significado=significado)
    session.add(nueva_palabra)
    session.commit()
    session.close()

def editar_palabra(palabra, nuevo_significado):
    session = Session()
    palabra_editar = session.query(Palabra).filter_by(palabra=palabra).first()
    palabra_editar.significado = nuevo_significado
    session.commit()
    session.close()

def eliminar_palabra(palabra):
    session = Session()
    palabra_eliminar = session.query(Palabra).filter_by(palabra=palabra).first()
    session.delete(palabra_eliminar)
    session.commit()
    session.close()

def listar_palabras():
    session = Session()
    palabras = session.query(Palabra).all()
    for palabra in palabras:
        print(f"{palabra.palabra}: {palabra.significado}")
    session.close()

def buscar_palabra(palabra):
    session = Session()
    palabra_encontrada = session.query(Palabra).filter_by(palabra=palabra).first()
    if palabra_encontrada:
        print(f"{palabra_encontrada.palabra}: {palabra_encontrada.significado}")
    else:
        print(f"No se encontró la palabra {palabra}")
    session.close()
