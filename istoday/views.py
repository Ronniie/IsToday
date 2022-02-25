from datetime import datetime
from django.shortcuts import render


# Create your views here.
def index(request, day=None):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day is None:
        # Get Today's Day, Month, Year
        day = datetime.today().strftime('%A')
        question = 'What day is it today?'
        answer = 'Today is ' + day + '!'
    else:
        # Verify Day
        if day in days:
            day = day.title()
            question = 'Is today ' + day + '?'
            if day == datetime.today().strftime('%A'):
                answer = 'Yes, it is ' + day + '!'
            else:
                answer = 'No, it is not ' + day + '!'
        else:
            question = "I don't understand that day"
            answer = 'Please try again.'

    return render(request, 'istoday/index.html', {'question': question, 'answer': answer})
