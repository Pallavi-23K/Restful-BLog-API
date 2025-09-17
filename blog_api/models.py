from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    posts = db.relationship("Post", backref="author", lazy=True)
    comments = db.relationship("Comment", backref="author", lazy=True)
    notifications = db.relationship("Notification", foreign_keys="Notification.user_id", back_populates="recipient", lazy=True)
    sent_notifications = db.relationship("Notification", foreign_keys="Notification.actor_id", back_populates="actor", lazy=True)
    followers = db.relationship("Follower", foreign_keys="Follower.followed_id", backref="followed", lazy=True)
    following = db.relationship("Follower", foreign_keys="Follower.follower_id", backref="follower", lazy=True)

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    comments = db.relationship("Comment", backref="post", lazy=True)
    likes = db.relationship("PostLike", backref="post", lazy=True)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    likes = db.relationship("CommentLike", backref="comment", lazy=True)

class PostLike(db.Model):
    __tablename__ = "post_likes"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    is_like = db.Column(db.Boolean, default=True)
    __table_args__ = (db.UniqueConstraint("post_id", "user_id", name="unique_post_user"),)

class CommentLike(db.Model):
    __tablename__ = "comment_likes"
    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    is_like = db.Column(db.Boolean, default=True)
    __table_args__ = (db.UniqueConstraint("comment_id", "user_id", name="unique_comment_user"),)

class Follower(db.Model):
    __tablename__ = "followers"
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    __table_args__ = (db.UniqueConstraint("follower_id", "followed_id", name="unique_follow"),)

class Notification(db.Model):
    __tablename__ = "notifications"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)   # Recipient
    actor_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)  # Actor
    type = db.Column(db.String(50), nullable=False)  # e.g. "follow", "like_post"
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=True)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    message = db.Column(db.String(256), nullable=False)  # required not nullable

    recipient = db.relationship("User", foreign_keys=[user_id], back_populates="notifications")
    actor = db.relationship("User", foreign_keys=[actor_id], back_populates="sent_notifications")
