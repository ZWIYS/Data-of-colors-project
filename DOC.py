# List of lists, dicts and tuple =)
List_main = {'Red': '#FF0000',
             'Orange': '#FFA500',
             'Yellow': '#FFFF00',
             'Green': '#008000',
             'Aqua': '#00FFFF',
             'Blue': '#0000FF',
             'Purple': '#800080'}

# dict with auth information!
AdminNames = {'Peter': '123456'}
SimpleNames = {'Guest': '0000'}

# function for remove sth from List
def Remove():
    Remove_item = input('input object from list to remove: ')
    if Remove_item in List_main:
        print(f'object: {Remove_item} removed')
        del List_main[Remove_item]
    else:
        print(f'this object doesnt exist in List: {Remove_item}')


def List_print():
    print(f'List: {List_main}')


# function for find sth in List
def information_about_List_main():
    Item_to_find = input('find sth from List:')
    if Item_to_find in List_main:
        Index_of_color = List_main[Item_to_find]
        print('this object in List:', Item_to_find)
        print('index of color is:', Index_of_color)
    else:
        print('this object doesnt exist in List:', Item_to_find)


# function for add sth in List
def add():
    Key_item = input('input key to add to List:')
    Object_to_key = input('input object to key:')
    print('object:', Key_item, 'added to list')
    List_main[Key_item] = Object_to_key


def commands():
    print('command list: find, add to list, list, remove, exit')



def main():
    # some infomation for users
    print('if you dont have admin licens use Name: Guest and Password: 0000')
    AdminCheck = -1
    while True:
        name = input('Name: ')
        passw = input('Password: ')
        if name in SimpleNames.keys() and passw == SimpleNames[name]:
            AdminCheck = False
            break
        elif name in AdminNames.keys() and passw == AdminNames[name]:
            AdminCheck = True
            break
        else:
            print('Uncorrect user name')

        if AdminCheck:
            print('command list: find, add to list, list, remove, command list, exit')
        else:
            print('command list: find, list, command list, exit')

        while True:
            command = input('command: ').lower()

            if command == 'add to list' and AdminCheck:
                add()

            elif command == 'find':
                information_about_List_main()

            elif command == 'list':
                List_print()

            elif command == 'remove' and AdminCheck:
                Remove()

            elif command == 'command list':
                commands()

            elif command == 'exit':
                if AdminCheck:
                    print('Admin, bye bye')
                else:
                    print('Guest, bye bye')
                break

            else:
                print('command doesnt exist')