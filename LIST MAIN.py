#List of lists, dicts and tuple =)
List_main={'Red':'#FF0000',
       'Orange':'#FFA500',
       'Yellow':'#FFFF00',
       'Green':'#008000',
       'Aqua':'#00FFFF',
       'Blue':'#0000FF',
       'Purple':'#800080'}

#tuple with auth information!
AuthName=('Peter',)

PassAuth=('123456',)


#function for remove sth from List
def Remove():
    Remove_item=input('input object from list to remove:')
    if remove_item in List_main:
        print('object:',Remove_item ,'removed')
        del List_main [Remove_item]
    else:
        print('this object doesnt exist in List:', Remove_item)
        
def List_print():
    print('List:', List_main)


#function for find sth in List
def information_about_List_main():
    Item_to_find = input('find sth from List:')
    if Item_to_find in List_main:
        Index_of_color = List_main[Item_to_find]
        print('this object in List:',Item_to_find)
        print('index of color is:', Index_of_color)
    else:
        print('this object doesnt exist in List:', Item_to_find)



#function for add sth in List
def add():
    Key_item = input('input key to add to List:')
    Object_to_key = input('input object to key:')
    print('object:', Key_item, 'added to list')
    List_main [Key_item] = Object_to_key

def commands():
    print('command list: find, add to list, list, remove, exit')


#some infomation for users
print('if you dont have admin licens use Name: Guest and Password: 0000')


#auth for guest

name = input('Name:')
passw = input ('Password:')

if name =='Guest' and passw == '0000':
    print('in Guest auth you dont have all permissions')
    print('command list: find, add to list, list, remove, command list, exit')

    while True:
        command=input('command:')

        if command == 'find':
            information_about_List_main()
            
        elif command == 'list':
            print(List_main)

        elif command == 'command list':
            commands()
            
        elif command == 'exit':
            print('Guest,bye bye')
            break

        elif command == 'add to list' or command == 'remove':
            print('You dont have permissions for this command')
            
        else:
            print('command doesnt exist')

    
#auth for Admin
            
if name in AuthName and passw in PassAuth:
    print('you use Admin licence')

    
    while True:
        
        print('command list: find, add to list, list, remove, command list, exit')
        command = input('command:')

        if command == 'add to list':
            add()

        elif command == 'find':
            information_about_List_main()

        elif command == 'list':
            List_print()

        elif command == 'remove':
            Remove()

        elif command == 'comand list':
            commands()

        elif command == 'exit':
            print('Admin, bye bye')
            break
        
        else:
            print('command doesnt exist')
else:
    print('incorrect Name or Password, try aganin (please, restart the program)')
