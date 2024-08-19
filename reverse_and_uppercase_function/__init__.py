import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    input_text = req.get_body().decode('utf-8')
    reversed_text_uppercase = input_text[::-1].upper()
    return func.HttpResponse(reversed_text_uppercase, status_code=200)
