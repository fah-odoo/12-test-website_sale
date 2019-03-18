import logging
from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)


class Child(models.Model):

    _inherit = 'ir.mail_server'

    def build_email(self, email_from, email_to, subject, body, email_cc=None, email_bcc=None, reply_to=False,
                    attachments=None, message_id=None, references=None, object_id=False, subtype='plain', headers=None,
                    body_alternative=None, subtype_alternative='plain'):
        

        _logger.warn(email_from)
        _logger.warn(tools.config.get(email_from))
        return super(Child,self).build_email(email_from, email_to, subject, body, email_cc=email_cc, email_bcc=email_bcc, reply_to=reply_to,
                    attachments=attachments, message_id=message_id, references=references, object_id=object_id, subtype=subtype, headers=headers,
                    body_alternative=body_alternative, subtype_alternative=subtype_alternative)