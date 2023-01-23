from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mailqueue.models import MailerMessage


"""
To get serializer errors from validation errors
"""


def generate_serializer_errors(args):
    message = ""
    for key, values in args.items():
        error_message = ""
        for value in values:
            error_message += value + ","
        error_message = error_message[:-1]

        message += f"{key} - {error_message} | "

    return message[:-3]


def send_email(to_address, subject, content, html_content, attachment=None, attachment2=None, attachment3=None, bcc_address=None):
    new_message = MailerMessage()
    new_message.subject = subject
    new_message.to_address = to_address
    if bcc_address:
        new_message.bcc_address = bcc_address
    new_message.from_address = "Safwan"
    new_message.content = content
    new_message.html_content = html_content
    if attachment:
        new_message.add_attachment(attachment)
    if attachment2:
        new_message.add_attachment(attachment2)
    if attachment3:
        new_message.add_attachment(attachment3)
    new_message.app = "default"
    new_message.save()


def paginate_items(items, number, page=1):
    paginated = Paginator(items, number)

    try:
        instance = paginated.page(page)
    except PageNotAnInteger:
        instance = paginated.page(1)
    except EmptyPage:
        instance = paginated.page(paginated.num_pages)

    has_next_page = False
    has_previous_page = False
    next_page_number = 1
    previous_page_number = 1

    if instance.has_next():
        has_next_page = True
        next_page_number = instance.next_page_number()

    if instance.has_previous():
        has_previous_page = True
        previous_page_number = instance.previous_page_number()

    paginated = {
        "current_page": instance.number,
        "has_next_page": has_next_page,
        "has_previous_page": has_previous_page,
        "next_page_number": next_page_number,
        "previous_page_number": previous_page_number,
        "total_pages": paginated.num_pages,
        "total_items": paginated.count,
        "first_item": instance.start_index(),
        "last_item": instance.end_index(),
    }

    paginated_data = {
        "data":instance.object_list,
        "paginated_data":paginated
    }

    return paginated_data