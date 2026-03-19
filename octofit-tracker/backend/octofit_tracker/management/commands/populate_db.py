from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from django.conf import settings

from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index('email', unique=True)

        # Sample users
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
        ]
        db.users.insert_many(users)

        # Sample teams
        teams = [
            {"name": "Marvel", "members": ["ironman@marvel.com", "cap@marvel.com", "widow@marvel.com"]},
            {"name": "DC", "members": ["superman@dc.com", "batman@dc.com", "wonderwoman@dc.com"]},
        ]
        db.teams.insert_many(teams)

        # Sample activities
        activities = [
            {"user": "superman@dc.com", "activity": "Flying", "duration": 60},
            {"user": "batman@dc.com", "activity": "Martial Arts", "duration": 45},
            {"user": "ironman@marvel.com", "activity": "Flight Suit Training", "duration": 50},
        ]
        db.activities.insert_many(activities)

        # Sample leaderboard
        leaderboard = [
            {"team": "Marvel", "points": 150},
            {"team": "DC", "points": 140},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Sample workouts
        workouts = [
            {"name": "Strength Training", "suggested_for": ["superman@dc.com", "cap@marvel.com"]},
            {"name": "Agility Drills", "suggested_for": ["batman@dc.com", "widow@marvel.com"]},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
