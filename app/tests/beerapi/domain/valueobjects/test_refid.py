import pytest
import uuid
from app.maindoapp.mainvalueobjects.refid import RefId


class TestRfid:

    def test_should_create(self):
        ref = uuid.uuid4()
        instance = RefId.create(ref)
        assert isinstance(instance, RefId)
        assert instance.value == ref

    def test_should_not_create_from_constructor_passing_none(self):
        ref = uuid.uuid4()
        with pytest.raises(AssertionError):
            RefId(ref, None)

    def test_should_not_create_from_constructor_passing_object(self):
        ref = uuid.uuid4()
        with pytest.raises(AssertionError):
            RefId(ref, object())

    def test_should_not_create_from_none(self):
        ref = None
        with pytest.raises(ValueError):
            RefId.create(ref)

    def test_should_not_create_from_empty(self):
        ref = ""
        with pytest.raises(ValueError):
            RefId.create(ref)

    def test_should_not_create_from_empty_with_blank_spaces(self):
        ref = "  "
        with pytest.raises(ValueError):
            RefId.create(ref)
