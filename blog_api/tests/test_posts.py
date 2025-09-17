# blog_api/tests/test_posts.py

def test_create_and_get_posts(client, auth_token):
    token = auth_token("poster", "p@example.com")

    # Create a post
    r = client.post("/posts", json={
        "title": "My First Post",
        "content": "This is the content"
    }, headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 201
    post_id = r.get_json()["post"]["id"]

    # Get all posts
    r = client.get("/posts")
    assert r.status_code == 200
    posts = r.get_json()["posts"]
    assert any(p["id"] == post_id for p in posts)


def test_update_and_delete_post(client, auth_token):
    token = auth_token("owner", "o@example.com")

    # Create post
    r = client.post("/posts", json={
        "title": "Temp Post",
        "content": "Will be updated"
    }, headers={"Authorization": f"Bearer {token}"})
    post_id = r.get_json()["post"]["id"]

    # Update post
    r = client.put(f"/posts/{post_id}", json={
        "title": "Updated Title",
        "content": "Updated content"
    }, headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.get_json()["post"]["title"] == "Updated Title"

    # Delete post
    r = client.delete(f"/posts/{post_id}", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.get_json()["message"] == "Post deleted successfully"
