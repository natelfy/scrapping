from scrape import extract_elements


def test_extract_elements_simple():
    html = "<html><body><p>Hello</p><div>Skip</div><p>World</p></body></html>"
    assert extract_elements(html, "p") == ["Hello", "World"]
