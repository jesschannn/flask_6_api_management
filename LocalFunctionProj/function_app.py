import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="feeling")
def emotion_get(req: func.HttpRequest) -> func.HttpResponse:
    emotion = req.params.get("emotion")
    if not emotion:
        emotion = "nothing"
    if emotion:
        return func.HttpResponse(f'Why are you feeling {emotion}?')