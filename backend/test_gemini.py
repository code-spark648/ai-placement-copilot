from google import genai

API_KEY = "AQ.Ab8RN6L7vXme4PrG5vpT7P0BHyp3IxMN3RFHy7Q96mOY0i-7Bg"

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello"
)

print(response.text)