try:
    from unittest import mock
except ImportError:
    import mock

import pytest


@pytest.fixture
def mock_render_to_string():
    def renderer(template_name, *args, **kwargs):
        if template_name.endswith('html'):
            return '<p>Some <strong>HTML</strong> content.</p>'

        return 'Some plain text content.'

    with mock.patch(
        'email_utils.render_to_string',
        side_effect=renderer,
    ) as mock_render:
        yield mock_render
