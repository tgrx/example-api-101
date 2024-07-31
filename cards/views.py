from cards.entities import CardEntity
from cards.entities import NewCardEntity
from cards.models import Card
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.views.generic import View
from project.entities import DataEntity
from project.entities import ErrorEntity


class CardsView(View):
    """
    A view for Cards.
    """

    def get(self, _request: HttpRequest) -> JsonResponse:
        """
        A handler for GET http request.
        Returns all cards, serialized, in JSON:API format.
        """

        cards = self._get_all_cards()
        payload = DataEntity[list[CardEntity]](data=cards).model_dump()
        return JsonResponse(payload)

    def post(self, request: HttpRequest) -> JsonResponse:
        """
        A handler for POST http request.
        Creates and returns a new card, using the incoming data.
        """

        try:
            payload_in = DataEntity[NewCardEntity].model_validate_json(request.body)
            new_card = self._create_new_card(payload_in.data)
            payload_out = DataEntity[CardEntity](data=new_card).model_dump()
            return JsonResponse(payload_out)

        except Exception as exc:  # noqa: BLE001
            payload_err = ErrorEntity(errors=[str(exc)]).model_dump()
            return JsonResponse(payload_err)

    def _get_all_cards(self) -> list[CardEntity]:
        """
        Returns all saved cards, as a list of entities.
        """

        cards = [CardEntity.model_validate(card) for card in Card.objects.all()]
        return cards

    def _create_new_card(self, data: NewCardEntity, /) -> CardEntity:
        """
        Creates a new Card entity using new card data.
        Returns a new Card entity.
        """

        kwargs = data.model_dump()
        new_card = Card.objects.create(**kwargs)
        new_entity = CardEntity.model_validate(new_card)

        return new_entity
