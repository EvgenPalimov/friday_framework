import urllib.parse


class ParseInputData:
    """
    The class - parses the request url parameters into a key and a value.
    """

    @staticmethod
    def parse(data: str) -> dict:
        """
        The function of parsing the request url.

        :param data: str: request url parameters,
        :return: dict: request url parameters.
        """
        result = {}
        value_to_list = ['courses', 'students', 'type_course']
        if data:
            data_decode = urllib.parse.unquote(data)
            params = data_decode.split('&')
            for item in params:
                k, v = item.split('=')
                if k in value_to_list:
                    if result.get(k, False):
                        result[k].append(v)
                    else:
                        result[k] = [v]
                else:
                    result[k] = v
        return result


class GetRequests(ParseInputData):
    """The class responsible for processing the GET request."""

    @staticmethod
    def get_request_params(environ) -> dict:
        """
        Function - extracting request url parameters and transmitting response.

        :param environ: dict: request data from the server,
        :return: dict: request url parameters
        """

        query_string = environ['QUERY_STRING']
        request_params = ParseInputData.parse(query_string)
        return request_params


class PostRequests(ParseInputData):
    """The class responsible for processing the POST request."""

    @staticmethod
    def get_wsgi_input_data(env) -> bytes:
        """
        The function checks for the presence of content in the request.

        Checks the length of the data, the content of the POST request,
        if the content is available, then reads it and returns it.

        :param env: dict: POST request parameters,
        :return: dict: request data or an empty byte string
        """

        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) \
            if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        """
        POST request data decoding function.

        The function accepts a string in the form of bytes.
        Decodes it and passes it to another function to extract data.
        Returns the received data.

        :param data: bytes: POST request data in byte format,
        :return: dict: POST request data.
        """

        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            result = ParseInputData.parse(data_str)
        return result

    def get_request_params(self, environ):
        """
        The main function of POST request processing.

        :param environ: dict: POST request parameters,
        :return: extracted POST request data/
        """
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
