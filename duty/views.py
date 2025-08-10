from django.shortcuts import render
from .forms import TextForm, AssessVal
import time
import bdtariff

# Create your views here.
def index(request):
    hscode = ''
    output = ''
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            try:
                if input_text.isdigit():
                    hscode = bdtariff.hscode(input_text)
            except IndexError:
                output = f"No information found for [{input_text}]."
            except Exception as e:
                print(f"An unexpected error for HSCode [{input_text}]: {e}")
            time.sleep(0.2)
    else:
        form = TextForm()

    return render(request, 'index.html', {'form': form, 'output': output, 'hscode': hscode})

def totalduty(request):
    cusduty = ''
    output = ''
    if request.method == 'POST':
        form = AssessVal(request.POST)
        if form.is_valid():
            hscodenbr = form.cleaned_data['hscodenbr']
            assval_text = eval(form.cleaned_data['assval_text'])
            try:
                if hscodenbr.isdigit():
                    cusduty = bdtariff.duty(hscodenbr,assval_text)
                else:
                    pass  
            except IndexError:
                output = f"No information found for [{hscodenbr}]."
            except Exception as e:
                print(f"An unexpected error for HSCode [{hscodenbr}]: {e}")
            time.sleep(0.2)
    else:
        form = AssessVal()

    return render(request, 'dutycal.html', {'form': form, 'output': output, 'cusduty': cusduty})