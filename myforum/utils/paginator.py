# coding:utf-8
from django.core.paginator import Paginator

def paginate_quervset(objs, page_no, cnt_per_page=10, half_show_length=5):
    p = Paginator(objs, cnt_per_page) #每页显示文章个数
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no < 0:
        page_no = 1
    page_links = [i for i in range(page_no - 5, page_no + 6) if i > 0 and i <= p.num_pages]
    page = p.page(page_no)
    previous_link = page_links[0] - 1
    next_link = page_links[-1] + 1

    has_previous = previous_link > 0
    has_next = next_link <= p.num_pages

    paginate_data = {"has_previous":has_previous,"has_next":has_next,
                     "previous_link":previous_link,
                     "next_link":next_link,
                     "page_cnt":p.num_pages,
                     "current_no":page_no,
                     "page_links":page_links
                     }
    return (page.object_list,paginate_data)