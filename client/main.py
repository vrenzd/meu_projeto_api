import requests

API_URL = "http://127.0.0.1:8000"

def analyze_sentiment(text: str):
    response = requests.post(f"{API_URL}/sentiment", json={"text": text})
    if response.status_code == 200:
        return response.json()
    else:
        try:
            error_detail = response.json().get("detail", response.text)
            print(f"Erro ao analisar o texto: {error_detail}")
        except Exception:
            print(f"Erro inesperado: {response.text}")
        return None

def main():
    print("Análise de Sentimentos (LeIA) - Digite 'sair' para encerrar.")
    while True:
        texto = input("Digite o texto para análise (máx 280 caracteres): ").strip()
        if texto.lower() == "sair":
            break
        if not texto:
            print("Por favor, insira algum texto.")
            continue

        resultado = analyze_sentiment(texto)
        if resultado:
            print(f"Scores: {resultado['scores']}\n")
        else:
            print("Nenhum resultado recebido.\n")

if __name__ == "__main__":
    main()
