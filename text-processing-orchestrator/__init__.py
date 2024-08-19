import requests
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    input_text = req.get_body().decode('utf-8')

    # Invoke reverse-and-uppercase function
    reversed_text_uppercase_response = requests.post("http://localhost:7072/api/reverse-and-uppercase", data=input_text).text

    # Invoke word-count function
    word_count_response = requests.post("http://localhost:7072/api/word-count", data=input_text).text

    # Combine outputs
    output = f"{reversed_text_uppercase_response}\n{word_count_response}"
    
    return func.HttpResponse(output, status_code=200)
