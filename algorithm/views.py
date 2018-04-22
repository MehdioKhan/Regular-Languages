from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.checks.security import csrf
from . import lang
from .forms import ContactForm


def home(request):
    return render(request, 'algorithm/home.html', {})


def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            c = form.save()
            c.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'algorithm/contact.html', {'form': form})


def nfa_to_dfa(request):
    alphabet = request.POST.get('alphabet').split(',')
    q = request.POST.get('q').split(',')
    q0 = request.POST.get('q0')
    f = request.POST.get('f').split(',')
    temp = request.POST.get('delta').replace('(', '').replace(')', '').split(',')
    delta = []
    for i in range(0,len(temp)-3,3):
        delta.append(tuple(temp[i:i+3]))

    nfa = lang.NFA(alphabet=alphabet, q=q, q0=q0, f=f, delta=delta)
    dfa = lang.nfa_to_dfa(nfa)
    data = {'alphabet': str(list(dfa.alphabet)).replace("'", ""), 'q': str(set_to_list(dfa.q)).replace("'", ""),
            'q0': str(list(dfa.q0)).replace("'", ""),
            'f': str(set_to_list(dfa.f)).replace("'", ""), 'delta': str(delta_to_list(dfa.delta)).replace("'", "")}
    if csrf.check_csrf_middleware:
        return JsonResponse(data, safe=False)


def set_to_list(input_list):
    output_list = []
    for l in input_list:
        if type(l) is set:
            output_list.append(list(l))
        else:
            output_list.append(l)
    return output_list


def delta_to_list(delta):
    output = []
    for d in delta:
        output.append((list(d[0]), d[1], list(d[2])))
    return output