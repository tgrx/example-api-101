from cards.entities import CardEntity
from cards.models import Card
from django.test import TestCase
from django.test.client import Client
from project.entities import DataEntity


class CardsTest(TestCase):
    def test_can_get_all_cards_when_no_cards(self, /) -> None:
        all_cards = self.get_all_cards()
        self.assertListEqual(all_cards, [])

    def test_can_get_all_cards_ordered(self, /) -> None:
        titles = ["Charlie", "Alpha", "Bravo"]
        installed_cards = [Card.objects.create(title=title) for title in titles]
        all_cards = self.get_all_cards()

        expected_cards_titles = sorted(card.title for card in installed_cards)
        got_cards_titles = [card.title for card in all_cards]

        self.assertListEqual(
            got_cards_titles,
            expected_cards_titles,
        )

    def test_can_create_card(self, /) -> None:
        title = "Alpha"
        self.assertFalse(
            Card.objects.filter(title=title).exists(),
            "no cards must be installed before the test",
        )

        api_card = self.create_card(title="Alpha")

        self.assertEqual(api_card.title, title)

        db_card = Card.objects.get(title=title)
        self.assertEqual(api_card.id, db_card.id)
        self.assertEqual(api_card.title, db_card.title)

    def setUp(self, /) -> None:
        super().setUp()
        self.client = Client()

    def get_all_cards(self) -> list[CardEntity]:
        response = self.client.get("/api/cards/")
        payload = DataEntity[list[CardEntity]].model_validate_json(response.content)
        return payload.data

    def create_card(
        self,
        /,
        *,
        content: str | None = None,
        title: str,
    ) -> CardEntity:
        data_in = {"title": title}
        if content:
            data_in["content"] = content

        payload_in = {"data": data_in}
        response = self.client.post("/api/cards/", payload_in, "application/json")
        payload_out = DataEntity[CardEntity].model_validate_json(response.content)

        return payload_out.data
