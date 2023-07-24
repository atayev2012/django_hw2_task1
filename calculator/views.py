from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_handle(request, recipe_name):
    if recipe_name not in DATA.keys():
        context = {
            "recipe": 0
        }
        return render(request, "calculator/index.html", context)
    else:
        qty = int(request.GET.get("servings", 1))
        context = {
            "recipe": DATA[recipe_name].copy()

        }

        for key in context["recipe"]:
            context["recipe"][key] = context["recipe"][key] * qty

        return render(request, "calculator/index.html", context)



