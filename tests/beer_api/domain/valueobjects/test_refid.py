import pytest
import uuid
from beer_api.domain.valueobjects.refid import RefId


class TestRfid:

    def test_should_create(self):
        ref = uuid.uuid4()
        instance = RefId.create(ref)
        assert isinstance(instance, RefId)
        assert instance.value == ref

    def test_should_not_create_from_constructor(self):
        ref = uuid.uuid4()
        with pytest.raises(AssertionError):
            RefId(ref, None)

        with pytest.raises(AssertionError):
            RefId(ref, object())

    def test_should_not_create_from_empty(self):
        ref = ""
        with pytest.raises(ValueError):
            RefId.create(ref)

        ref = None
        with pytest.raises(ValueError):
            RefId.create(ref)

    def test_should_not_create_from_empty_with_blank_spaces(self):
        ref = "  "
        with pytest.raises(ValueError):
            RefId.create(ref)

        ref = None
        with pytest.raises(ValueError):
            RefId.create(ref)