from fastapi.exceptions import HTTPException
from fastapi import status



class APIError(HTTPException):
    def __init__(self, key, **params):
        error_obj = ErrorMessages(key, **params)
        super().__init__(status_code=error_obj.status_code,
            detail=error_obj.message
        )


class ErrorMessages:
    ERRORS = {
        # tuple of reason, message
        'unauthorized': (
            status.HTTP_401_UNAUTHORIZED,
            'Unauthorized',
            'Unauthorized',
        ),
        'unauthorized_w_msg': (
            status.HTTP_401_UNAUTHORIZED,
            'Unauthorized',
            '%(text)s',
        ),
        'authorization_error': (
            status.HTTP_403_FORBIDDEN,
            'Authorization error',
            '%(text)s',
        ),
        'not_found': (
            status.HTTP_404_NOT_FOUND,
            'Not found',
            '%(field)s "%(value)s" does not exist',
        ),
        'not_found_general': (
            status.HTTP_404_NOT_FOUND,
            'Not found',
            '%(value)s not found',
        ),
        # unlike other not found errors this one returns 400 to show that user try invalid resource access.
        'not_found_resource': (
            status.HTTP_400_BAD_REQUEST,
            'Not found',
            '%(field)s "%(value)s" does not exist',
        ),
        'missing_field': (
            status.HTTP_404_NOT_FOUND,
            'Missing field',
            '%(field)s field is missing',
        ),
        'required_list': (
            status.HTTP_400_BAD_REQUEST,
            'Required field',
            'Please select at least one %(field)s',
        ),
        'required_field': (
            status.HTTP_400_BAD_REQUEST,
            'Required field',
            '%(field)s can not be empty',
        ),
        'invalid_field': (
            status.HTTP_400_BAD_REQUEST,
            'Invalid field',
            'Please enter valid "%(field)s"',
        ),
        'invalid_field_value': (
            status.HTTP_400_BAD_REQUEST,
            'Invalid value',
            'Field: "%(field)s" has invalid value: "%(value)s"',
        ),
        'invalid_field_value_with_expected': (
            status.HTTP_400_BAD_REQUEST,
            'Invalid value',
            'Field: "%(field)s" has invalid value: "%(value)s". %(expected_note)s',
        ),
        'invalid_value': (
            status.HTTP_400_BAD_REQUEST,
            'Invalid value',
            'Please enter valid post data. "%(value)s"',
        ),
        'duplicated_resource': (
            status.HTTP_400_BAD_REQUEST,
            'Duplicated resource',
            'Duplicated %(value)s object',
        ),
        'conflicted_with_detail': (
            status.HTTP_400_BAD_REQUEST,
            'Duplicated resource',
            'Duplicated %(value)s object. %(text)s',
        ),
        'general_error': (
            status.HTTP_400_BAD_REQUEST,
            'Error',
            '%(text)s',
        ),
    }

    def __init__(self, key, **params):
        self.key = key
        self.params = params

    @property
    def status_code(self):
        return self.ERRORS[self.key][0]

    @property
    def reason(self):
        return self.ERRORS[self.key][1]

    @property
    def message(self):
        error_message = self.ERRORS[self.key][2]
        # apply text arguments
        return error_message % self.params
