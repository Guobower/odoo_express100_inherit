# -*- coding: utf-8 -*-
from odoo import http

# class Myodoo(http.Controller):
#     @http.route('/myodoo/myodoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myodoo/myodoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myodoo.listing', {
#             'root': '/myodoo/myodoo',
#             'objects': http.request.env['myodoo.myodoo'].search([]),
#         })

#     @http.route('/myodoo/myodoo/objects/<model("myodoo.myodoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myodoo.object', {
#             'object': obj
#         })