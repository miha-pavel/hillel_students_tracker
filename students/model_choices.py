GET, POST, DELETE, PUT, PATCH, HEAD, CONNECT, OPTIONS, TRACE = 0, 1, 2, 3, 4, 5, 6, 7, 8
METHOD = (
    (GET, 'GET'), (POST, 'POST'), (DELETE, 'DELETE'), (PUT, 'PUT'), (PATCH, 'PATCH'),
    (HEAD, 'HEAD'), (CONNECT, 'CONNECT'), (OPTIONS, 'OPTIONS'), (TRACE, 'TRACE'),
    )
METHODS_REVERSED_MAP = {name: id for id, name in METHOD}