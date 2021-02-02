from src.domain.models import Beer
from src.application.queries import ListBeerQuery, GetBeerByIDQuery


def test_list_beers():
    """
    GIVEN 2 beers stored in the database
    WHEN the execute method is called
    THEN it shoud return 2 beers
    """
    Beer(
        name='Budweiser',
        kind='Larger',
        origin='USA',
        alcohol='5'
    ).save()

    Beer(
        name='Eisenbahn',
        kind='Strong Golden Ale',
        origin='Brasil',
        alcohol='8.5'
    ).save()

    query = ListBeerQuery()

    assert len(query.execute()) == 2


def test_get_beer_by_id():
    """
    GIVEN ID of beer stored in the database
    WHEN the execute method is called on GetBeerByQuerry with id
    THEN it shoud return the beer with same id
    """

    beer = Beer(
        name='Budweiser',
        kind='Larger',
        origin='USA',
        alcohol='5'
    ).save()

    query = GetBeerByIDQuery(id=beer.id)
    result = query.execute()
    assert result.id == beer.id
