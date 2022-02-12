# coding: utf-8

import json
import requests
from sentry.plugins.bases.notify import NotificationPlugin

import sentry_feishu
from .forms import FeiShuOptionsForm


class FeiShuPlugin(NotificationPlugin):
    """
    Sentry plugin to send error counts to FeiShu.
    """
    author = 'john shine'
    author_url = 'https://github.com/john-shine/sentry-feishu-webhook'
    version = sentry_feishu.VERSION
    description = 'Send errors exceptions to FeiShu Webhook.'
    resource_links = [
        ('Source', 'https://github.com/john-shine/sentry-feishu-webhook'),
        ('Bug Tracker', 'https://github.com/john-shine/sentry-feishu-webhook/issues'),
        ('README', 'https://github.com/john-shine/sentry-feishu-webhook/blob/master/README.md'),
    ]

    slug = 'FeiShu'
    title = 'FeiShu'
    conf_key = slug
    conf_title = title
    project_conf_form = FeiShuOptionsForm
    timeout = 5

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('url', project))

    def do_send(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        url = self.get_option('url', group.project)
        text = u"{}: {}. To view more detail visit {}".format(event.project.slug, event.message, group.get_absolute_url())

        data = {
            "msg_type": "text",
            "content": {
                "text": text,
            }
        }

        requests.post(
            url=url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8"),
            timeout=self.timeout,
        )

    def notify_users(self, group, event, *args, **kwargs):
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        self.do_send(group, event, *args, **kwargs)
