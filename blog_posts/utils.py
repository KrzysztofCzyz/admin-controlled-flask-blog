from blog_posts import db
from blog_posts.models import PostHeader, PostMetadata, PostContent, Post
from blog_posts.vms import PostHeaderVM, PostVM

# TODO - add cache to get_post_headers


def get_post_headers():
    raw_posts = list()
    raw_posts = db.session.query(PostHeader, PostMetadata)\
        .filter(PostHeader.post_id == PostMetadata.post_id)\
        .all()
    result_posts = PostHeaderVM().map(raw_posts)
    return result_posts


def get_post_vm_by_id(post_id):
    post = Post.query\
        .filter(Post.id == post_id)\
        .first()
    if post is not None:
        post_vm = PostVM.map(post)
        return post_vm
    return None
