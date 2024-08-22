from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone', 'email', 'branch', 'value_for_money', 
                  'packaging', 'quality', 'display', 'variety', 'comments', 
                  'employee_name_id', 'voice_message_base64']

    def clean_voice_message_base64(self):
        """Optional: Clean and validate the Base64 data."""
        voice_message_base64 = self.cleaned_data.get('voice_message_base64')
        
        # Optionally, you can add validation for the base64 data here
        if voice_message_base64:
            # Example of simple validation (e.g., checking if it's a valid base64 string)
            if not voice_message_base64.startswith('data:audio/webm;base64,'):
                raise forms.ValidationError("Invalid audio data format.")
        
        return voice_message_base64
