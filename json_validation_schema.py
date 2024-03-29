json_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "id": {"type": "integer"}
    },
    "required": ["userId", "title", "body", "id"]
}