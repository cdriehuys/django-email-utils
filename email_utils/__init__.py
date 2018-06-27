from django.core import mail
from django.template.loader import render_to_string


def send_email(template_name, context=None, *args, **kwargs):
    """
    Send a templated email.

    To generate the message used for the email, the method first
    searches for an HTML template with the given name
    (eg: <template>.html), and renders it with the provided context. The
    process is repeated for the plain text message except a 'txt'
    extension is used. All other options are forwarded to Django's
    ``send_mail`` function.

    Args:
        template_name:
            The name of the template to use without an extension. The
            extensions ``html`` and ``txt`` are appended to the template
            name and then rendered to provide the email content.
        context:
            A dictionary containing the context to render the message
            with. Defaults to an empty dictionary.

    Returns:
        ``1`` if the email is succesfully sent and ``0`` otherwise. The
        return values come from Django's ``send_mail`` function.
    """
    context = context or {}

    html = render_to_string(
        context=context,
        template_name='{}.html'.format(template_name),
    )
    text = render_to_string(
        context=context,
        template_name='{}.txt'.format(template_name),
    )

    return mail.send_mail(
        *args,
        html_message=html,
        message=text,
        **kwargs
    )
