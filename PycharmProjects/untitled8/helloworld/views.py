from django.http import HttpResponse


def index(request):
    # print('reuqest:', request, type(request))
    # print(dir(request))
    response = HttpResponse(
        """<html>
            <h1>HELLO</h1>
            <b> World</b>
            <br />
            <br />
            <br />
            <hr />
            <b> Salam </b>
        </html>""",
        status=404
    )
    return response

def bye(request):
    response = HttpResponse(
        "Bye Bye"
    )
    return response