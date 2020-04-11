from blog_posts.models import PostHeader, PostMetadata
from datetime import datetime, timedelta

# TODO - map time better, exchange authorId for author's name
# TODO - check queries for relations between posts and related tables


class PostHeaderVM:

    @staticmethod
    def map(*args):
        mapped_posts = list()
        for posts in args:
            for header, metadata in posts:
                last_updated = round((datetime.utcnow() - metadata.created).total_seconds())
                mapped_posts.append({
                    'post-id': header.post_id,
                    'title': header.title,
                    'lead': header.lead_text,
                    'content': 'First post content',
                    'contentId': 1,
                    'lastUpdated': last_updated,
                    'authorId': metadata.author_id,
                    'leadImage': header.lead_graphic
                })
        return mapped_posts

