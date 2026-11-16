def test_build_url(api_client):
    url = api_client._build_url("/posts/1")

    assert url == "https://jsonplaceholder.typicode.com/posts/1"
