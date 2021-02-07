class EntityNotFoundException(Exception):
    exception_id = "exception:entity_not_found"

    def __init__(self, ref_id: str, entity_name: str):
        message = f"'{entity_name}' with was not found."
        self._message = message

        super(EntityNotFoundException, self).__init__(message)

    @property
    def message(self):
        return self._message
