from root.models import Team, FrequentlyQuestion,Leader
from django.contrib.auth.models import User


def repeated_objects(request):

    users_count = User.objects.all().count()
    teams = Team.objects.filter(status=True)
    team_count = teams.count()
    questions = FrequentlyQuestion.objects.filter(status=True)
    context = {
        "teams" : teams,
        "questions" : questions, 
        "tc" : team_count,
        "uc" : users_count,

    }
    return context