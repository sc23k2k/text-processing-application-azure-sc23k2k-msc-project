import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    input_text = req.get_body().decode('utf-8')
    reversed_text_uppercase = input_text[::-1].upper()
    
    # Calculate word count
    words = input_text.split()
    word_count = len(words)

    # Combine outputs
    output = f"Reversed Text (uppercase): {reversed_text_uppercase}\nWord Count: {word_count}"
    
    return func.HttpResponse(output, status_code=200)
