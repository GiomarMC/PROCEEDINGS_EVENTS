from abc import ABC, abstractmethod

class Evento:
    def __init__(self, id=None, nombre=None, fecha=None, descripcion=None, hora=None, lugar=None, edicion_id=None):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion
        self.hora = hora
        self.lugar = lugar
        self.edicion_id = edicion_id

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None,
            "descripcion": self.descripcion,
            "hora": self.hora.isoformat() if self.hora else None,
            "lugar": self.lugar,
            "edicion_id": self.edicion_id
        }
    
    @staticmethod
    def from_dict(data):
        return Evento(
            id=data.get('id'),
            nombre=data.get('nombre'),
            fecha=data.get('fecha'),
            descripcion=data.get('descripcion'),
            hora=data.get('hora'),
            lugar=data.get('lugar'),
            edicion_id=data.get('edicion_id')
        )

class EventoRepositorio(ABC):
    """Interfaz para el repositorio de Evento. Define métodos CRUD esenciales."""

    @abstractmethod
    def crear(self, evento: Evento):
        """Crea un nuevo evento en la base de datos.

        Args:
            evento (Evento): El evento a ser creado.
        """
        pass

    @abstractmethod
    def obtener(self, id: int) -> Evento:
        """Obtiene un evento por su ID.

        Args:
            id (int): El ID del evento a buscar.

        Returns:
            Evento: El evento encontrado o None si no se encuentra.
        """
        pass

    @abstractmethod
    def actualizar(self, evento: Evento):
        """Actualiza un evento existente en la base de datos.

        Args:
            evento (Evento): El evento con los datos actualizados.
        """
        pass

    @abstractmethod
    def eliminar(self, id: int) -> Evento:
        """Elimina un evento de la base de datos por su ID.

        Args:
            id (int): El ID del evento a eliminar.
        """
        pass