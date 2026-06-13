# poetry init

"""
Создай класс Album у которого есть поля

- Исполнитель (artist) - строка
- Название (title) - строка
- Треки (tracks) - список

Создай два экземпляра album_1 и album_2

Исполнитель: Queen
Название: Killer Queen
Треки: Brighton rock, Killer Queen, Tenement Funster

Исполнитель: Metallica
Название: Black Album
Треки: Enter Sandman, Sad But True, Holier Than Thou
"""


class Album:
    """Класс, описывающий музыкальный альбом"""

    def __init__(self, artist: str, title: str, tracks: list):
        """Инициализация полей альбома"""
        self.artist = artist  # Исполнитель
        self.title = title  # Название
        self.tracks = tracks  # Список треков


# Создаем два экземпляра (объекта) класса Album
album_1 = Album(
    artist="Queen",
    title="Killer Queen",
    tracks=["Brighton rock", "Killer Queen", "Tenement Funster"],
)


album_2 = Album(
    artist="Metallica",
    title="Black Album",
    tracks=["Enter Sandman", "Sad But True", "Holier Than Thou"],
)


# код для проверки
print(
    album_1.artist, album_1.title, len(album_1.tracks), "треков"
)  # >>> Queen Killer Queen 3 треков
print(
    album_2.artist, album_2.title, len(album_2.tracks), "треков"
)  # >>> Metallica Black Album 3 треков
