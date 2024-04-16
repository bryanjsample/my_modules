from directory import Directory, get_key_press
import os
import subprocess
from typing import List
import sys
from time import sleep

class ItemsToOpen(Directory):
    '''
    
    '''
    def __init__(self, target_extension:bool | str=False):
        Directory.__init__(self, target_extension)
        self.__target_items:List[str] = self.choose_multiple_items()
        self.__item_paths:List[str] = [f'{self.Directory_Path}/{item_name}' for item_name in self.Target_Items]

    @property
    def Target_Items(self) -> List[str]:
        return self.__target_items

    @property
    def Item_Paths(self) -> List[str]:
        return self.__item_paths

    def open_items(self):
        def one_at_at_time():
            for path in self.Item_Paths:
                open_confired = get_key_press(message=f'\nPress enter to open {path} or any other key to continue.', pressed_any_other=False)
                if open_confired:
                    subprocess.run(['open', '-g', path])

        def all_at_once():
            self.Item_Paths.insert(0, 'open')
            subprocess.run(self.Item_Paths)
        os.system('clear')
        get_key_press(message=f'\nPress enter to open {', '.join(self.Target_Items)} all at once or any other key to open one at a time...', pressed_enter=all_at_once, pressed_any_other=one_at_at_time)
        os.system('clear')
        print('All files successfully opened.')

def main():
    items = ItemsToOpen(sys.argv[1:])
    items.open_items()

if __name__ == "__main__":
    main()