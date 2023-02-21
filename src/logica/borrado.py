from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
  session = Session()
  cancion2 = session.query(Cancion).get(2)
  if cancion2 != None:
    session.delete(cancion2)
    session.commit()
  else:
    print("El registro no existe.")
  session.close()
