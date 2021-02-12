class RepositoryException(Exception):
    error_id = "exception:repository"

    def __init__(self, repository: str, message: str):
        self._repository = repository
        self._message = message

        super(RepositoryException, self).__init__(message)

    @property
    def repository(self):
        return self._repository

    @property
    def message(self):
        return self._message
