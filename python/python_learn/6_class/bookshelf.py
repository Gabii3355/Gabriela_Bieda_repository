#!/usr/bin/python3
class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author 
        self.pages=pages

    def __str__(self): #returns back string representation
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

#    def __del__(self):
#        print(f'Your book {self.title} has been deleted from the bookshelf')

book1=Book('My first book','Me',223)
print(str(book1))
print(len(book1))

