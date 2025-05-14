from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Red Rockets')
        team2 = Team.objects.create(name='Blue Blasters')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_points=5)
        workout2 = Workout.objects.create(name='Running', description='Run 1 mile', suggested_points=10)
        workout3 = Workout.objects.create(name='Jump Rope', description='Jump rope for 5 minutes', suggested_points=7)

        # Activities
        Activity.objects.create(user=user1, activity_type='Pushups', duration=10, points=5)
        Activity.objects.create(user=user2, activity_type='Running', duration=20, points=10)
        Activity.objects.create(user=user3, activity_type='Jump Rope', duration=5, points=7)

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=15)
        Leaderboard.objects.create(team=team2, points=7)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
