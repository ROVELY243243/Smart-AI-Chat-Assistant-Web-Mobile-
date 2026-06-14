from django.http import JsonResponse
from django.shortcuts import render
from openai import OpenAI

client = OpenAI(api_key="TA_CLE_API_ICI ")

def chat_page(request):
    return render(request, "chatbot/chat.html")


def ask(request):
    message = request.GET.get("message", "")

    if not message:
        return JsonResponse({"reply": "Écris quelque chose 🙂"})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Tu es un assistant intelligent, clair et utile."},
                {"role": "user", "content": message}
            ]
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = "Erreur IA ❌ vérifie ta clé API"

    return JsonResponse({"reply": reply})