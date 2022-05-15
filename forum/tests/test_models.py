# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from forum.models import Topic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestTopicModel(TestCase):
    """Test Topic model"""
    def setUp(self):
        self.topic = Topic.objects.create(
            name="Coding",
            friendly_name="Coding",
            slug="Coding",
            topic_image="topic_img",

            )

    def test_topic_model_instance(self):
        """
        This test tests the topic model
        """
        topic = self.topic
        self.assertTrue(isinstance(topic, Topic))

    def test_topic_model_str_method(self):
        """ Test Topic model string method """
        topic = self.topic
        self.assertEqual((topic.__str__()), topic.name)

    def test_topic_model_function_friendly_name(self):
        """ Test Topic model function friendly
            returns friendly name 
        """
        topic_friendly_name = self.topic.friendly_name
        self.assertEqual(str(topic_friendly_name), "Coding")
    