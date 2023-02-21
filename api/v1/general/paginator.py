from django.core.paginator import Paginator as P, EmptyPage, PageNotAnInteger


class Paginator:
    """
        custom paginator
    """
    def __init__(self,instances:list=None,count:int=None,page:int=1):
        self.paginated = P(instances, count)

        try:
            instance = self.paginated.page(page)
        except PageNotAnInteger:
            instance = self.paginated.page(1)
        except EmptyPage:
            instance = self.paginated.page(self.paginated.num_pages)

        self.objects = instance.object_list
        """
            pagnated objects
        """
        self.current_page = instance.number
        """
            current page number
        """
        self.total_pages = self.paginated.num_pages
        """
            total pages of instance
        """
        self.total_items = self.paginated.count
        """
            Total paginated items count
        """
        self.first_item = instance.start_index()
        """
            index of first item in the current page
        """
        self.last_item = instance.end_index()
        """
            index of last item in the current page
        """
        self.has_next_page = False
        """
            has next page
        """
        self.has_previous_page = False
        """
            has previous page
        """
        self.next_page_number = 1
        """
            next page number 
        """
        self.previous_page_number = 1
        """
            previous page number 
        """

        if instance.has_next():
            self.has_next_page = True
            self.next_page_number = instance.next_page_number()

        if instance.has_previous():
            self.has_previous_page = True
            self.previous_page_number = instance.previous_page_number()
