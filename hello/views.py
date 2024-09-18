
from django.shortcuts import render, redirect
from datetime import date
from .forms import AddParticipantForm
import random

# Перевірка, чи сьогодні Різдво
def is_christmas(request):
    today = date.today()
    is_christmas_day = (today.month == 12 and today.day == 25)

    context = {
        'is_christmas': is_christmas_day,
        'today': today,
    }

    return render(request, 'hello/is_christmas.html', context)

def secret_santa(request):
    if 'participants' not in request.session:
        request.session['participants'] = []

    participants = request.session['participants']
    pairs = None
    error_message = None

    # Додавання учасника
    if request.method == 'POST' and 'add_participant' in request.POST:
        form = AddParticipantForm(request.POST)
        if form.is_valid():
            participant = form.cleaned_data['participant'].strip()

            if participant and participant not in participants:
                participants.append(participant)
                request.session['participants'] = participants
            else:
                error_message = "Цей учасник уже в списку або ім'я порожнє."

    # Видалення учасника
    elif request.method == 'POST' and 'remove_participant' in request.POST:
        participant_to_remove = request.POST.get('participant_name')
        if participant_to_remove in participants:
            participants.remove(participant_to_remove)
            request.session['participants'] = participants

    # Генерація пар для всіх учасників
    elif request.method == 'POST' and 'generate_pairs' in request.POST:
        if len(participants) < 2:
            error_message = "У списку має бути щонайменше дві людини!"
        else:
            givers = participants[:]
            receivers = participants[:]
            random.shuffle(receivers)

            pairs = []
            for giver in givers:
                receiver = random.choice(receivers)
                while receiver == giver:
                    receiver = random.choice(receivers)
                pairs.append((giver, receiver))
                receivers.remove(receiver)

    # Очищення списку учасників
    elif request.method == 'POST' and 'clear_participants' in request.POST:
        request.session['participants'] = []
        return redirect('secret_santa')

    form = AddParticipantForm()

    return render(request, 'hello/secret_santa.html', {
        'form': form,
        'participants': participants,
        'pairs': pairs,
        'error_message': error_message
    })
