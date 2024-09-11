todo_list=[]

def add_task():
    task=input('Enter a task to the To-Do List:')
    todo_list.append(task)
    print(f'{task} has been successfully added!')

def display_tasks():
    if(len(todo_list)==0):
        print('There are no tasks to display.')
    else:
        print('Your tasks are:')
        num=1
        for z in todo_list:
            print(f'{num}.{z}')
            num+=1

def remove_task():
    if (len(todo_list)==0):
        print('There are no task to display.')    
    
    task_no=int(input('Enter the task number to be removed:'))
    list_length=len(todo_list)
    
    if (task_no<1 or task_no>list_length):
        print('Invailed task number.')
    else:
        todo_list.pop(task_no-1)
        print(f'Task {task_no} has been successfully removed.')
        
def main():
    print('Welcome to To-Do List Application')
    print('Enter 1 to add a task')
    print('Enter 2 to display all task')
    print('Enter 3 to delete a task')
    print('Enter 4 to exit')
    
    while True:
        choice=int(input('Enter your choice from 1 to 4:'))
        if choice==1:
            add_task()
        elif choice==2:
            display_tasks()
        elif choice==3:
            remove_task()
        elif choice==4:
            print('Exiting the app.')
            break

main()