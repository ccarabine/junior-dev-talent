# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column, Layout, Field
from crispy_forms.bootstrap import FormActions
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    A class for post forms
    """
    class Meta:
        model = Post
        fields = ("title", "body", "post_image")

    def __init__(self, *args, **kwargs):
        """
        Set title,body,post image label to falsel and
        Set placeholders for title and body
        Show title, body, post_image and submit button
        Args:
            self (object): Self object
            *args: *args
            **kwargs: **kwargs
        Returns:
            N/A
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.fields['title'].label = False
        self.fields['body'].label = False
        self.fields["post_image"].label = False

        self.helper.layout = Layout(
            Field(
                "title",
                placeholder="Title"),
            Field(
                "body",
                placeholder="Description"),
            Row(
                Column(
                    Field(
                        "post_image",
                        placeholder="Image Upload")),

                FormActions(
                    Submit(
                        "submit",
                        "Submit post",
                        css_class="btn btn-secondary"
                        )
                ),
            ),
        )
class CommentForm(forms.ModelForm):
    """
    A class for comments
    """
    class Meta:
        model = Comment
        fields = ("comment_body",)

    def __init__(self, *args, **kwargs):
        """
        Set commentbody label to false and show comment body and submit button
        Args:
            self (object): Self object
            *args: *args
            **kwargs: **kwargs
        Returns:
            N/A
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["comment_body"].label = False
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Field("comment_body"),
            Submit(
                "submit",
                "Add Comment",
                css_class="btn btn-secondary"),
        )
