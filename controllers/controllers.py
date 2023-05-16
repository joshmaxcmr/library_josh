# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryJosh(http.Controller):
#     @http.route('/library_josh/library_josh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_josh/library_josh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_josh.listing', {
#             'root': '/library_josh/library_josh',
#             'objects': http.request.env['library_josh.library_josh'].search([]),
#         })

#     @http.route('/library_josh/library_josh/objects/<model("library_josh.library_josh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_josh.object', {
#             'object': obj
#         })
