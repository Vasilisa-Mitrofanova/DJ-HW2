from django.shortcuts import render
from django.shortcuts import HttpResponse

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

def test(request, recipe):
    our_recipe = DATA[recipe]
    servings = int(request.GET.get('servings', 1))
    new_recipe = {}
    for x in our_recipe:
        new_recipe[x]=our_recipe[x]*servings
    context = {
        'recipe': new_recipe,
        'servings': int(servings)
    }
    #return HttpResponse(str(context))
    return render(request, 'recipe_temp.html', context)
