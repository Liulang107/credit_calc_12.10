from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    if request.method == "GET":
        form = CalcForm(request.GET)
        if form.is_valid():
            initial_fee = form.cleaned_data['initial_fee']
            rate = form.cleaned_data['rate']
            months_count = form.cleaned_data['months_count']
            common_result = round((initial_fee + initial_fee * (rate / 100)), 2)
            result = round((common_result / months_count), 2)
            context = {
                'form': form,
                'result': result,
                'common_result': common_result,
            }
        else:
            context = {
                'form': form,
            }

    return render(request, template, context)
