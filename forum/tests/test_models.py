# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.auth.models import User

# Internal:
from forum.models import Topic, Post, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestTopicModel(TestCase):
    """Test Topic model"""
    def setUp(self):
        chris_c = User.objects.create_user(
            username='chris_c', password='p2word')

        self.topic = Topic.objects.create(
            name="Coding",
            friendly_name="Coding",
            slug="Coding",
            topic_image="topic_img",
            )
        self.post = Post.objects.create(
            topic=self.topic,
            title="interview question",
            owner=chris_c,
            slug="interview%question"
        )
        self.comment = Comment.objects.create(
            post=self.post,
            owner=chris_c,
            comment_body="Great idea",
            name="Chris Carabine"
        )

    def tearDown(self):
        """
        Delete test user, topic, post and comment
        """
        User.objects.all().delete()
        Topic.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()

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

    def test_post_model_str_method(self):
        """ Test Post model string method """
        post = self.post
        self.assertEqual((post.__str__()), post.title)

    def test_post_model_get_absolute_url(self):
        """ Test get_absolute_url """
        post = self.post
        self.assertEquals(str(post.get_absolute_url()), '/forum/topic/1')

    def test_comment_model_str_method(self):
        """ Test Comment model string method """
        comment = self.comment
        self.assertEquals(str(comment), 'Comment Great idea by Chris Carabine')

    def test_comment_model_get_absolute_url(self):
        """ Test get_absolute_url """
        comment = self.comment
        self.assertEquals(str(comment.get_absolute_url()), '/forum/topic/1')
