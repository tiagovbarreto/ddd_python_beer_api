import pytest

from app.models import Beer
from app.commands import CreateBeerCommand, AlreadyExists


def test_create_beer():
    """"
    GIVEN CreateBeerCommand with valid properties name, brand and alcohol
    WHEN the execute method is called
    THEN a new Beer must exist in the database with the samet attributes
    """
    cmd = CreateBeerCommand(
        name='Budweiser',
        kind='Larger',
        origin='USA',
        alcohol='5'
    )

    beer = cmd.execute()

    db_beer = Beer.get_by_id(beer.id)

    assert db_beer.id == beer.id
    assert db_beer.name == beer.name
    assert db_beer.kind == beer.kind
    assert db_beer.origin == beer.origin
    assert db_beer.alcohol == beer.alcohol


def test_create_beer_already_exists():
    """
    GIVEN CreateBeerCommand with a name of some beer in database
    WHEN the execute method is called
    THEN the AlreadyExists exception must be raised
    """

    Beer(
        name='Budweiser',
        kind='Larger',
        origin='USA',
        alcohol='5'
    ).save()

    cmd = CreateBeerCommand(
        name='Budweiser',
        kind='Larger',
        origin='USA',
        alcohol='5'
    )

    with pytest.raises(AlreadyExists):
        cmd.execute()
