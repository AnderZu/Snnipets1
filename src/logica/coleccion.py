from src.modelo.album import Album, Medio
from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.declarative_base import engine, Base, session

class Coleccion():
    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_album(self, titulo, anio, descripcion, medio):
        busqueda = session.query(Album).filter(Album.titulo == titulo).all()
        if len(busqueda) == 0:
            album = Album(titulo=titulo, ano=anio, descripcion=descripcion, medio=medio)
            session.add(album)
            session.commit()
            return True
        else:
            return False

    def dar_medios(self):
        return [medio.name for medio in Medio]

    def editar_album(self, album_id, titulo, anio, descripcion, medio):
        busqueda = session.query(Album).filter(Album.titulo == titulo, Album.id != album_id).all()
        if len(busqueda) == 0:
            album = session.query(Album).filter(Album.id == album_id).first()
            album.titulo = titulo
            album.ano = anio
            album.descripcion = descripcion
            album.medio = medio
            session.commit()
            return True
        else:
            return False

    def eliminar_album(self, album_id):
        try:
            album = session.query(Album).filter(Album.id == album_id).first()

            session.delete(album)
            session.commit()
            return True
        except:
            return False

    def dar_album_por_id(self, album_id):
        return session.query(Album).get(album_id).__dict__

if __name__ == '__main__':
    # Crea la BD
    Base.metadata.create_all(engine)
    coleccion = Coleccion()

    if coleccion.agregar_album("abc1", 2021, "Album original", Medio.DISCO):
        print("Se añadio el nuevo registro.")
    else:
        print("Ya existe el titulo. No se añadio el registro.")

    if coleccion.editar_album(1, "zxy", 2022, "Primicia", Medio.CASETE):
        print("Se actualizó el registro.")
    else:
        print("Ya existe el titulo. No se actualizó el registro.")

