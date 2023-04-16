from django.test import TestCase
from .models import Project, Thumbnail
from datetime import datetime


# Create your tests here.
class ProjectTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        end_date_string = "2023-04-16 16:30:00"
        cls.project = Project.objects.create(
            title="test project",
            details="test detail",
            end_date=datetime.strptime(end_date_string, "%Y-%m-%d %H:%M:%S"),
            category="education",
            tags="test",
        )
        cls.thumbnail = Thumbnail.objects.create(
            image_url="https://picsum.photos/200/300",
            project=cls.project,
        )

    def test_Project_model(self):
        end_date_string = "2023-04-16 16:30:00"
        self.assertEquals(self.project.title, "test project")
        self.assertEquals(self.project.details, "test detail")
        self.assertEquals(
            self.project.end_date,
            datetime.strptime(end_date_string, "%Y-%m-%d %H:%M:%S"),
        )
        self.assertEquals(self.project.category, "education")
        self.assertEquals(self.project.tags, "test")
        self.assertEquals(str(self.project), "test project")
        self.assertEquals(Project.objects.count(), 1)

    def test_thumbnail_model(self):
        self.assertEquals(self.thumbnail.image_url, "https://picsum.photos/200/300")
        self.assertEquals(self.thumbnail.project.category, "education")
        self.assertEquals(str(self.thumbnail.project), "test project")
        self.assertEquals(str(self.thumbnail), "test project")
        self.assertEquals(Thumbnail.objects.count(), 1)
