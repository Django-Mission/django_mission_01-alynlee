from cgitb import reset
import random
from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def calculator(request):

    # 0. request 확인
    print(f"request = {request}")
    print(f"request doc = {request.__doc__}")
    print(f"request class = {request.__class__}")

    # 1. 데이터 확인
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    operators = request.GET.get("operators")

    # 2. 계산
    if operators == "+":
        result = int(num1) + int(num2)
    elif operators == "-":
        result = int(num1) + int(num2)
    elif operators == "*":
        result = int(num1) * int(num2)
    elif operators == "/":
        result = int(num1) / int(num2)
    else:
        result = 0

    # 3. 응답
    return render(request, "calculator.html", {"result": result})


def lotto(request):

    return render(request, "lotto.html")


def lotto_result(request):

    result = [random.sample(range(1, 46), 7) for _ in range(3)]
    game_num = request.GET.get("game_num")

    return render(
        request, "lotto_result.html", {"result": result, "game_num": game_num}
    )
