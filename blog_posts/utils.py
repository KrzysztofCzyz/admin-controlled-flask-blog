from blog_posts.models import PostHeader


def get_post_headers():
    result_posts = PostHeader.query().all()
    return result_posts

