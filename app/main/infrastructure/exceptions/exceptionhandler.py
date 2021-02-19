import logging
from flask import Blueprint, Response, jsonify, json

_logger = logging.Logger(__name__)


error_handler_bp = Blueprint('handle_error', __name__)


@error_handler_bp.app_errorhandler(Exception)
def handle_error(error):
    print(error)
    status_code = int(error.status_code)
    message = error.message
    error_code = error.error_code

    log = "{}:[ {} ] {}".format(status_code, error_code, message)

    log_by_status = {
        401: _logger.warning,
        403: _logger.warning,
        400: _logger.exception,
        404: _logger.exception,
        422: _logger.exception,
        500: _logger.error,
    }

    log_by_status.get(status_code, lambda m: _logger.warning)(log)

    return Response(
        response=json.dumps(dict(code=status_code, message=message)),
        status=status_code,
        content_type="application/json",
    )
    return jsonify(error=str(e.code)), code
