from app.models import Beer
from app.queries import ListBeerQuery


def test_list_beers():
    """
    GIVEN 2 beers stored in the database
    WHEN the execute method is called
    THEN it shoud return 2 beers
    """
    Beer(
        name='Budweiser',
        type='Larger',
        origin='USA',
        alcohol='5'
    ).save()

    Beer(
        name='Eisenbahn',
        type='Strong Golden Ale',
        origin='Brasil',
        alcohol='8.5'
    ).save()

    query = ListBeerQuery()

    assert len(query.execute()) == 2
