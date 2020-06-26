# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vessel(models.Model):
    _name = 'vessel.vessel'
    _rec_name = 'name'
    _description = 'Vessels'

    name = fields.Char(string="Vessel Name")
    type = fields.Selection(string="Vessel Type",
                            selection=[('mother', 'Mother'), ('daughter', 'Daughter'), ], required=False, )


class VesselProgramme(models.Model):
    _name = 'vessel.programme'
    _rec_name = 'programme_id'
    _description = 'Vessel Programme Information'

    programme_id = fields.Char(string="Program Identification", default=lambda self: _('New'), requires=False,
                               readonly=True, trace_visibility='onchange',)
    date = fields.Date(string="Date of Programme", required=False, )
    revised_date = fields.Date(string="Revised Programme")
    product_id = fields.Many2one(comodel_name="product.vessel", string="Product", required=False, )
    qty_mt = fields.Integer(string="Quantity (MT)", required=False, )
    qty_litre = fields.Integer(string="Quantity (Litres)", required=False,)
    discharge_port = fields.Char(string="Discharge Port", required=False, )
    location = fields.Char(string="Location", required=False,)
    armed_clear_apply = fields.Date(string="Armed Clearance Application Date", required=False)
    armed_clear_approve = fields.Date(string="Armed Clearance Approval Date", required=False)
    armed_clear_duration = fields.Integer(string="Armed Clearance Duration", required=False)
    armed_clear_expiry = fields.Date(string="Date of Expiry of Armed guard Clearance", required=False)
    armed_clear_status = fields.Selection(string="Status of Reapplication",
                                          selection=[('active', 'Active'), ('expired', 'Expired'), ], required=False, )
    navy_clear = fields.Date(string="Navy Clearance Date", required=False, )

    @api.model
    def create(self, vals):
        if vals.get('programme_id', _('New')) == _('New'):
            vals['programme_id'] = self.env['ir.sequence'].next_by_code('increment_programme_id') or _('New')
        result = super(VesselProgramme, self).create(vals)
        return result


class ProductVessel(models.Model):
    _name = 'product.vessel'
    _rec_name = 'name'
    _description = 'Products'

    name = fields.Char()
