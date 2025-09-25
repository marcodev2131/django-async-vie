# views.py
import asyncio
import httpx
from django.http import HttpResponse
import traceback

async def async_view(request):
    try:
        # simula trabalho assíncrono e imprime 1..5 no terminal
        for num in range(1, 6):
            await asyncio.sleep(1)
            print(num)

        # faz uma chamada HTTP assíncrona e imprime o resultado no terminal
        async with httpx.AsyncClient() as client:
            r = await client.get("https://httpbin.org/get")
            print("Status:", r.status_code)
            print("URL:", r.json().get("url"))

        return HttpResponse("Exercicio assíncrono concluído! Verifique o terminal para ver a saída.")
    except Exception:
        tb = traceback.format_exc()
        print("Erro na async_view:", tb)
        return HttpResponse(f"Erro interno no servidor:<br><pre>{tb}</pre>", status=500)
