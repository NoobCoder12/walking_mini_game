from game import Game
import pytest


@pytest.fixture
def game():
    return Game()


def test_found_chest(game):
    game.chest_found()
    assert game.chests == 1
    assert game.gold > 0


def test_nothing_found(game):
    game.nothing_found()
    assert game.nothing == 1
