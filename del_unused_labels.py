from todoist_api_python.api import TodoistAPI

API_TOKEN = "API_TOKEN"
api = TodoistAPI(API_TOKEN)

def main():
    # get labels
    labels = api.get_labels()  # labels list
    # get tasks
    tasks = api.get_tasks()  # tasks list
    # collect used labels
    used = set()
    for task in tasks:
        for lab in task.labels:
            used.add(lab)
    # delete unused labels
    for label in labels:
        if label.name not in used:
            print(f"deleting {label.name}")
            api.delete_label(label.id)

if __name__ == "__main__":
    main()
