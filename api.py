import paralleldots
paralleldots.set_api_key("iH4OCc3pwUFUjRcoyzug4ShpopFEtpLFigQEZlmmk")

def ner(text):
    ner=paralleldots.ner(text)
    return ner