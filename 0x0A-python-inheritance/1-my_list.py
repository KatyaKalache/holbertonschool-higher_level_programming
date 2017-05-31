#!/usr/bin/python3
class MyList(list):
    list = []

    def print_sorted(self):
        MyList.list.append(self)
        for i in self.list:
            print(sorted(i))
