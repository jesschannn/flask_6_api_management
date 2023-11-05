import azure.functions as func
import logging

app = func.FunctionApp()
@app.function_name(name="test")
@app.route(route='feeling')

@func.httptrigger(methods=['GET', 'POST'], route="feeling")
def feeling(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    emotion = req.params.get('emotion')
    if not emotion:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            emotion = req_body.get('emotion')

    if emotion:
        return func.HttpResponse(f"Why are you feeling {emotion}?")
    else:
        return func.HttpResponse(
            "Why are you feeling nothing?"
        )