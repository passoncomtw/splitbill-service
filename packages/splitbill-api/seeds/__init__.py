user_data = {
    "model": "models.users.Users",
    "data": [
        {"id": 1, "name": "John March", "line_id": "john_line", "user_tag": "book"},
        {"id": 2, "name": "Tony Yang", "line_id": "tony_line", "user_tag": "game"},
        {"id": 3, "name": "Rob T", "line_id": "rob_line", "user_tag": "game"},
        {"id": 4, "name": "Tom H", "line_id": "tom_line", "user_tag": "sell"},
    ],
}

groups_data = {
    "model": "models.groups.Groups",
    "data": [
        {"id": 1, "name": "Party Night", "user_count": 1},
        {"id": 2, "name": "Shopping", "user_count": 1},
    ],
}

group_users_data = {
    "model": "models.group_users.Group_Users",
    "data": [
        {"id": 1, "user_id": 1, "group_id": 1},
        {"id": 2, "user_id": 2, "group_id": 2},
    ],
}

data = [user_data, groups_data, group_users_data]
