class EntityNotFoundByRefIdError(Exception):
    error_id = "error:entity_not_found"

    def __init__(self, ref_id: str, entity_name: str):
        message = f"'{entity_name}' with ref ID '{ref_id}' was not found."
        self._message = message

        super(EntityNotFoundByRefIdError, self).__init__(message)

    @property
    def message(self):
        return self._message
