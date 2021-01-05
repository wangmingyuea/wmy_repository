import json
users = {
  "apps_count": 6,
  "page_size": 20,
  "items": [
    {
      "id": "59bf8e26959d69523e000177",
      "user_id": "1",
      "org_id": "59bba986548b7a1688812a7c",
      "type": "android",
      "name": "yljk",
      "short": "yx9a",
      "bundle_id": "01",
      "genre_id": 0,
      "web_template": "default",
      "custom_market_url": "",
      "created_at": 1505725990,
      "updated_at": 1505726002,
      "expired_at": 1505898802,
      "icon_url": "https://XXXXXX.com",
      "master_release": {
        "version": "1.0.0",
        "build": "1",
        "release_type": "inhouse",
        "distribution_name": ""

      }
    },
    {
      "id": "2",
      "user_id": "2",
      "org_id": "XXXXXX",
      "type": "android",
      "name": "wld",
      "short": "bpdb",
      "bundle_id": "XXXXXX",
      "genre_id": 0,
      "web_template": "default",
      "custom_market_url": "",
      "icon_url": "https://XXXXXX.com",
      "master_release": {
        "version": "1.0.0",
        "build": "1",
        "release_type": "inhouse",
        "distribution_name": ""
      }
    },
    {
      "id": "3",
      "user_id": "3",
      "org_id": "XXXXXX",
      "type": "android",
      "name": "wzlj",
      "short": "1tdc",
      "bundle_id": "XXXXXX",
      "genre_id": 0,
      "web_template": "default",
      "custom_market_url": "",
      "icon_url": "https://XXXXXX.com",
      "master_release": {
        "version": "1.0.0",
        "build": "1",
        "release_type": "inhouse",
        "distribution_name": ""
      }
    },
    {
      "id": "5",
      "user_id": "XXXXXX",
      "org_id": "XXXXXX",
      "type": "android",
      "name": "maib",
      "short": "y6td",
      "bundle_id": "XXXXXX",
      "genre_id": 0,
      "web_template": "default",
      "custom_market_url": "",
      "icon_url": "https://XXXXXX.com",
      "master_release": {
        "version": "1.0.0",
        "build": "1",
        "release_type": "inhouse",
        "distribution_name": ""
      }
    },
    {
      "id": "6",
      "user_id": "6",
      "org_id": "XXXXXX",
      "type": "android",
      "name": "jieb",
      "short": "jg3e",
      "bundle_id": "XXXXXX",
      "genre_id": 0,
      "web_template": "default",
      "custom_market_url": "",
      "icon_url": "https://XXXXXX.com",
      "master_release": {
        "version": "1.0.0",
        "build": "1",
        "release_type": "inhouse",
        "distribution_name": ""
      }
    }
  ]
}

new = []
for user in users['items']:
    new.append({
        'uname': user['name'],
        'ushort': user['short']
    })
print(new)
print ("你好")
