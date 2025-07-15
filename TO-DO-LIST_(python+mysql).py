import datetime as dt
d=dt.datetime.now()
date=d.strftime('%d-%m-%Y')

import mysql.connector as sql
db=sql.connect(host='localhost',user='root',password='Gaurav@07',database='project')
cur=db.cursor()

def add_task():
    try:
        print('\n---ADD TASK---\n')
        n = int(input('Enter the number of task(s) you want to add - '))
        cur.execute('create table if not exists todolist (TASK_ID int primary key auto_increment, DATE varchar(10) not null ,TASK_TITLE varchar(20) not null, TASK_DESCRIPTION varchar(100) not null, TASK_STATUS varchar(15) default "PENDING")')
        for i in range(1, n + 1):
            tt = input(f"Task {i} - ")
            td = input(f"Task Description {i} - ")
            print('Task added!\n')
            cur.execute('insert into todolist (DATE,TASK_TITLE,TASK_DESCRIPTION) values (%s,%s,%s)', (date, tt, td))
        print(f"You have successfully added {n} number of task(s)!\n")
    except:
        print('Something went wrong! Please try again.\n')

def view_task():
    try:
        print('\n---VIEW TASK---\n')
        cur.execute('select * from todolist')
        all=cur.fetchall()
        if all:
            print('Task ID, Date, Task Title, task Description, Status')
            print('-'*51)
            for i in all:
                print(i)
        else:
            print('No task(s) to show!\n')
    except:
        print('\nPlease Add Task(s) first!\n')

def del_task():
    try:
        print('\n---DELETE TASK---\n')
        delete = int(input('Enter TASK ID to delete the Task - '))
        cur.execute('select * from todolist where task_id=%s', (delete,))
        all = cur.fetchall()
        if all:
            for i in all:
                print(f"\nThe below task has been successfully deleted!")
                print(i)
                cur.execute('delete from todolist where task_id=%s', (delete,))
        else:
            print('\nTask not available! Please re-view the available task(s) first.\n')
    except:
        print('\nPlease Add Task(s) first!\n')

def update_task():
    try:
        print('\n---UPDATE TASK---\n')
        up = int(input('Enter TASK ID to update the task - '))
        cur.execute('select * from todolist where task_id=%s', (up,))
        x = cur.fetchall()
        if x:
            new_tt = input('Enter the new Task Title - ')
            new_td = input('Enter the new Task Description - ')
            cur.execute('update todolist set task_title=%s where task_id=%s', (new_tt, up))
            cur.execute('update todolist set task_description=%s where task_id=%s', (new_td, up))
            print('\nTask updated!\n')
        else:
            print('\nTask not found!\n')
    except:
        print('\nPlease Add Task(s) first!\n')

def mark_done():
    print('\n---MARK TASK AS COMPLETED---\n')
    n=int(input('Enter TASK ID to mark as "COMPLETED" - '))
    cur.execute('select * from todolist where task_id=%s',(n,))
    z=cur.fetchall()
    if z:
        cur.execute('update todolist set task_status="COMPLETED" where task_id=%s',(n,))
        print(f"Task ID {n} has been marked as 'Completed'!")
    else:
        print('\nTask not found!\n')

def pending_task():
    try:
        print('\n---SHOW PENDING TASK(S)---\n')
        cur.execute('select * from todolist where task_status="pending"')
        z = cur.fetchall()
        if z:
            print('All your "PENDING" task(s) - \n')
            print('Task ID, Date, Task Title, task Description, Status')
            print('-' * 51)
            for i in z:
                print(i)
        else:
            print('\nNo "PENDING" Task(s) available!\n')
    except:
        print('\nPlease Add Task(s) first!\n')

def completed_task():
    try:
        print('\n---SHOW COMPLETED TASK(S)---\n')
        cur.execute('select * from todolist where task_status="completed"')
        z = cur.fetchall()
        if z:
            print('All your "COMPLETED" task(s) - \n')
            print('Task ID, Date, Task Title, task Description, Status')
            print('-' * 51)
            for i in z:
                print(i)
        else:
            print('No "COMPLETED" Task(s) available!\n')
    except:
        print('\nPlease Add Task(s) first!\n')

def todolist():
    try:
        print('\n===TO DO LIST===\n')
        while True:
            menu = int(input('\n---MENU---\n1 - ADD TASK\n2 - VIEW TASK\n3 - DELETE TASK\n4 - UPDATE TASK\n5 - MARK TASK AS COMPLETED\n6 - SHOW PENDING TASK(S)\n7 - SHOW COMPLETED TASK(S)\n8 - EXIT TO SAVE CHANGES (if any)\nEnter your choice (from 1 to 7) - '))
            if menu == 1:
                add_task()
            elif menu == 2:
                view_task()
            elif menu == 3:
                del_task()
            elif menu == 4:
                update_task()
            elif menu == 5:
                mark_done()
            elif menu == 6:
                pending_task()
            elif menu == 7:
                completed_task()
            elif menu == 8:
                print('\nGoodbye for now!\n')
                break
    except:
        print('\nINVALID INPUT!\n')

todolist()

db.commit()
cur.close()
db.close()