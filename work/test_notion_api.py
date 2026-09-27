import requests
import json

token = "ntn_S524744796040qepWOGBLItfPGOgfb3bp4zYJ4MbVxZ9ai"
page_id = "3cb138c5b39880fe8b37e6ed03e1be79"

headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

# 1. Check Page
url_page = f"https://api.notion.com/v1/pages/{page_id}"
r = requests.get(url_page, headers=headers)
print("Page status:", r.status_code)
if r.status_code == 200:
    data = r.json()
    title_props = data.get("properties", {}).get("title", {}).get("title", [])
    title_text = "".join([t.get("plain_text", "") for t in title_props])
    print("Page Title:", title_text or data.get("properties"))
else:
    print("Page response:", r.text)

# 2. Check Blocks Children
url_blocks = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=50"
r_blocks = requests.get(url_blocks, headers=headers)
print("Blocks status:", r_blocks.status_code)
if r_blocks.status_code == 200:
    blocks = r_blocks.json().get("results", [])
    print(f"Retrieved {len(blocks)} blocks:")
    for b in blocks:
        b_type = b.get("type")
        content = ""
        if b_type in b:
            rich_texts = b[b_type].get("rich_text", [])
            content = "".join([rt.get("plain_text", "") for rt in rich_texts])
            if not content and "title" in b[b_type]:
                content = b[b_type].get("title", "")
        print(f"- [{b_type}] {content[:80]}")
else:
    print("Blocks response:", r_blocks.text)
