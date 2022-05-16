# Im# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages

# Internal:
from forum.models import Topic, Post, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestTopicModel(TestCase):
    """Test Topic model"""
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='chris_c', password='p2word')
        self.client.login(username='chris_c', password='p2word')
        self.user.save()

        self.topic = Topic.objects.create(
            name="Coding",
            friendly_name="Coding",
            slug="Coding",
            topic_image="topic_img",
            )
        self.post = Post.objects.create(
            topic=self.topic,
            title="interview question",
            owner=self.user,
            slug="interview%question"
        )
        self.comment = Comment.objects.create(
            post=self.post,
            owner=self.user,
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

    def test_get_list_of_topics(self):
        """
        This test tests get a list of topics and verifies
        checks
        1. that the status code is 200
        2. Templates used is forum.html
        3. Topic is Coding
        """
        response = self.client.get('/forum/')
        topic = Topic.objects.get()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/forum.html')
        self.assertTrue(topic, "Coding")

    def test_get_list_of_posts_not_loggedin(self):
        """
        This test tests get a list of posts  when not logged in and verifies
        checks
        A not logged in user is redirected to the login page and
        the status code is 302
        """
        self.client.logout()
        response = self.client.get('/forum/Coding/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/forum/Coding/')

    def test_get_list_of_posts_logged_in(self):
        """
        This test tests get a list of posts  when logged in and verifies
        checks
        A logged in user status code is 302
        """
        self.client.login(username='chris_c', password='p2word')
        response = self.client.get('/forum/Coding/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forum/post_list.html')

