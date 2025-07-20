import json

sample_tasks = [
    {
        "title": "Buy groceries",
        "category": "Personal",
        "completed": False
    },
    {
        "title": "Finish project report",
        "category": "Work",
        "completed": True
    },
    {
        "title": "Call the electrician",
        "category": "Personal",
        "completed": False
    }
]

with open("todo_list.json", "w") as file:
    json.dump(sample_tasks, file, indent=4)

print("todo_list.json created with sample tasks!")
