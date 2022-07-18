from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

from blog import models

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_posts_by_author(root, info, username):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )
schema = graphene.Schema(query=Query)