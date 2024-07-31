from project.entities import Entity


class CardEntity(Entity):
    content: str | None = None
    id: int
    title: str


class NewCardEntity(Entity):
    content: str | None = None
    title: str
