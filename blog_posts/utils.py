from blog_posts import db
from blog_posts.models import PostHeader, PostMetadata
from blog_posts.vms import PostHeaderVM


def get_post_headers():
    raw_posts = db.session.query(PostHeader, PostMetadata)\
        .filter(PostHeader.post_id == PostMetadata.post_id)\
        .all()
    result_posts = PostHeaderVM().map(raw_posts)
    return result_posts

