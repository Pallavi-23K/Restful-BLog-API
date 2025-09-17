# blog_api/tests/test_comments.py

def test_comment_lifecycle(client, auth_token):
    token = auth_token("charlie", "c@example.com")

    # Create post
    r = client.post("/posts", json={
        "title": "Commented Post",
        "content": "Post body"
    }, headers={"Authorization": f"Bearer {token}"})
    post_id = r.get_json()["post"]["id"]

    # Add comment
    r = client.post(f"/posts/{post_id}/comments", json={
        "content": "Nice post!"
    }, headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 201
    comment_id = r.get_json()["comment"]["id"]

    # Get comments
    r = client.get(f"/posts/{post_id}/comments")
    assert r.status_code == 200
    comments = r.get_json()["comments"]
    assert any(c["id"] == comment_id for c in comments)

    # Update comment
    r = client.put(f"/comments/{comment_id}", json={
        "content": "Edited comment"
    }, headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.get_json()["comment"]["content"] == "Edited comment"

    # Delete comment
    r = client.delete(f"/comments/{comment_id}", headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.get_json()["message"] == "Comment deleted successfully"
