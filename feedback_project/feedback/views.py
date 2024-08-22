from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
import base64
import re
from django.core.files.base import ContentFile

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Save the form data
            feedback = form.save(commit=False)
            
            # Handle Base64 audio data
            voice_message_base64 = form.cleaned_data.get('voice_message_base64')
            if voice_message_base64:
                # Extract the actual Base64 data (without the metadata prefix)
                base64_data = re.sub('^data:audio/webm;base64,', '', voice_message_base64)
                # Convert Base64 data to binary data
                audio_file = ContentFile(base64.b64decode(base64_data), 'voice_message.webm')
                feedback.voice_message.save('voice_message.webm', audio_file)
            
            feedback.save()
            return render(request, 'feedback/feedback_success.html')
    else:
        form = FeedbackForm()
    
    return render(request, 'feedback/Index.html', {'form': form})
