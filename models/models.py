# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class library_josh(models.Model):
#     _name = 'library_josh.library_josh'
#     _description = 'library_josh.library_josh'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
