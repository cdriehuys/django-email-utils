try:
    from unittest import mock
except ImportError:
    import mock

import email_utils


@mock.patch('email_utils.mail.send_mail')
def test_send_email(mock_send, mock_render_to_string):
    """
    The send email function should load the plain text and HTML versions
    of the template, and send an email with them.
    """
    html = mock_render_to_string('foo.html')
    text = mock_render_to_string('foo.txt')

    context = {'foo': 'bar'}
    from_email = 'no-reply@example.com'
    recipient_list = ['test@example.com']
    subject = 'Test Email'
    template_name = 'foo'

    email_utils.send_email(
        context=context,
        from_email=from_email,
        recipient_list=recipient_list,
        subject=subject,
        template_name=template_name,
    )

    # Twice to get values for test, and twice in the method itself
    assert mock_render_to_string.call_count == 4
    assert mock_render_to_string.call_args_list[2][1] == {
        'context': context,
        'template_name': '{}.html'.format(template_name),
    }
    assert mock_render_to_string.call_args_list[3][1] == {
        'context': context,
        'template_name': '{}.txt'.format(template_name),
    }

    assert mock_send.call_count == 1
    assert mock_send.call_args[1] == {
        'from_email': from_email,
        'html_message': html,
        'message': text,
        'recipient_list': recipient_list,
        'subject': subject,
    }
