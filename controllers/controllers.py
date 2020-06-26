# -*- coding: utf-8 -*-
from odoo import http

# class VesselManagementSystem(http.Controller):
#     @http.route('/vessel_management_system/vessel_management_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vessel_management_system/vessel_management_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vessel_management_system.listing', {
#             'root': '/vessel_management_system/vessel_management_system',
#             'objects': http.request.env['vessel_management_system.vessel_management_system'].search([]),
#         })

#     @http.route('/vessel_management_system/vessel_management_system/objects/<model("vessel_management_system.vessel_management_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vessel_management_system.object', {
#             'object': obj
#         })