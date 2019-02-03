# -*- coding: utf-8 -*-

from odoo import models,fields,api


class AccountInvoice(models.Model):
	_inherit = "account.invoice"
	number = fields.Char(related='move_id.name', store=True, readonly=False, copy=False)