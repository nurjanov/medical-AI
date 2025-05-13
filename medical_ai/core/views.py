from django.shortcuts import render, redirect
from .forms import MedicalImageForm
from .models import MedicalImage

def index(request):
    return render(request, 'core/index.html')

def upload(request):
    if request.method == 'POST':
        form = MedicalImageForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # Вставляем заглушку анализа
            instance.result = "Результат анализа: Нет признаков патологии (пример)"
            instance.save()
            return redirect('result', pk=instance.pk)
    else:
        form = MedicalImageForm()
    return render(request, 'core/upload.html', {'form': form})

def result(request, pk):
    image = MedicalImage.objects.get(pk=pk)
    return render(request, 'core/result.html', {'image': image})

     