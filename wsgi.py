#!/usr/bin/env python
import os

def application(environ, start_response):

    ctype = 'text/plain'
    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    else:
        ctype = 'text/html'
        response_body = '''

1x1=1&nbsp;1x2=2&nbsp;1x3=3&nbsp;1x4=4&nbsp;1x5=5&nbsp;1x6=6&nbsp;1x7=7&nbsp;1x8=8&nbsp;1x9=9&nbsp;<br />2x1=2&nbsp;2x2=4&nbsp;2x3=6&nbsp;2x4=8&nbsp;2x5=10&nbsp;2x6=12&nbsp;2x7=14&nbsp;2x8=16&nbsp;2x9=18&nbsp;<br />3x1=3&nbsp;3x2=6&nbsp;3x3=9&nbsp;3x4=12&nbsp;3x5=15&nbsp;3x6=18&nbsp;3x7=21&nbsp;3x8=24&nbsp;3x9=27&nbsp;<br />4x1=4&nbsp;4x2=8&nbsp;4x3=12&nbsp;4x4=16&nbsp;4x5=20&nbsp;4x6=24&nbsp;4x7=28&nbsp;4x8=32&nbsp;4x9=36&nbsp;<br />5x1=5&nbsp;5x2=10&nbsp;5x3=15&nbsp;5x4=20&nbsp;5x5=25&nbsp;5x6=30&nbsp;5x7=35&nbsp;5x8=40&nbsp;5x9=45&nbsp;<br />6x1=6&nbsp;6x2=12&nbsp;6x3=18&nbsp;6x4=24&nbsp;6x5=30&nbsp;6x6=36&nbsp;6x7=42&nbsp;6x8=48&nbsp;6x9=54&nbsp;<br />7x1=7&nbsp;7x2=14&nbsp;7x3=21&nbsp;7x4=28&nbsp;7x5=35&nbsp;7x6=42&nbsp;7x7=49&nbsp;7x8=56&nbsp;7x9=63&nbsp;<br />8x1=8&nbsp;8x2=16&nbsp;8x3=24&nbsp;8x4=32&nbsp;8x5=40&nbsp;8x6=48&nbsp;8x7=56&nbsp;8x8=64&nbsp;8x9=72&nbsp;<br />9x1=9&nbsp;9x2=18&nbsp;9x3=27&nbsp;9x4=36&nbsp;9x5=45&nbsp;9x6=54&nbsp;9x7=63&nbsp;9x8=72&nbsp;9x9=81&nbsp;<br />


'''

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body.encode('utf-8') ]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()
