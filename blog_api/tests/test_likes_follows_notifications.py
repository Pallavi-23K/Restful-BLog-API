# blog_api/tests/test_likes_follows_notifications.py

def test_like_and_unlike_post(client, auth_token):
    token = auth_token("dave", "d@example.com")

    # Create a post
    r = client.post("/posts", json={
        "title": "Likeable Post",
        "content": "Like this!"
    }, headers={"Authorization": f"Bearer {token}"})
    post_id = r.get_json()["post"]["id"]

    # Like post
    r = client.post(f"/posts/{post_id}/like", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.get_json()["liked"] is True

    # Unlike post
    r = client.post(f"/posts/{post_id}/like", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.get_json()["liked"] is False


def test_follow_and_unfollow_user(client, auth_token):
    t1 = auth_token("u1", "u1@example.com")
    t2 = auth_token("u2", "u2@example.com")

    # u1 follows u2
    r = client.post("/follow/u2", headers={"Authorization": f"Bearer {t1}"})
    assert r.status_code == 200
    assert r.get_json()["message"] == "Now following"

    # u1 unfollows u2
    r = client.post("/follow/u2", headers={"Authorization": f"Bearer {t1}"})
    assert r.status_code == 200
    assert r.get_json()["message"] == "Unfollowed"


def test_notifications_basic(client, auth_token):
    t1 = auth_token("notify", "n@example.com")
    t2 = auth_token("actor", "a@example.com")

    # actor creates a post
    r = client.post("/posts", json={
        "title": "Notify Post",
        "content": "Ping!"
    }, headers={"Authorization": f"Bearer {t2}"})
    post_id = r.get_json()["post"]["id"]

    # notify user follows actor
    client.post("/follow/actor", headers={"Authorization": f"Bearer {t1}"})

    # actor likes own post (just to generate a notification)
    client.post(f"/posts/{post_id}/like", headers={"Authorization": f"Bearer {t2}"})

    # check notifications
    r = client.get("/notifications", headers={"Authorization": f"Bearer {t1}"})
    assert r.status_code == 200
    notifications = r.get_json()["notifications"]
    assert len(notifications) >= 1
