import math
class Pagination:
    def __init__(self,items=[],page_size=10) -> None:
        self.items=items
        self.page_size=page_size
        self.current_page=0
        self.index=0
        self.total_pages=math.ceil(len(self.items)/self.page_size)

    def get_visible_items(self):
        self.index=(self.current_page*self.page_size)
        return self.items[self.index:(self.index + self.page_size)]
    

    def go_to_page(self,page_num:int):
        if page_num >= self.total_pages:
            raise ValueError()
        self.current_page=page_num
        return self.get_visible_items()

    def first_page(self):
        self.go_to_page(0)
        return self

    def last_page(self):
        self.go_to_page(self.total_pages-1)
        return self

    def next_page(self):
        self.go_to_page(self.current_page + 1)
        return self
    
    def prev_page(self):
        self.go_to_page(self.current_page - 1)
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p=Pagination(alphabetList,3)

print(p.get_visible_items(),p.current_page,p.total_pages)
p.last_page().next_page()
print(p.get_visible_items(),p.current_page)





