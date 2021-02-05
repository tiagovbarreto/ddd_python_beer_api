class RepositoryError(Exception):
    error_id = "error:repository"

    def __init__(self, repository: str, message: str):
        self._repository = repository
        self._message = message

        super(RepositoryError, self).__init__(message)

    @property
    def repository(self):
        return self._repository

    @property
    def message(self):
        return self._message
