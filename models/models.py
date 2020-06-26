# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import datetime
from datetime import date



class Vessel(models.Model):
    _name = 'vessel.vessel'
    _rec_name = 'name'
    _description = 'Vessels'

    name = fields.Char(string="Vessel Name")
    type = fields.Selection(string="Vessel Type",
                            selection=[('mother', 'Mother'), ('daughter', 'Daughter'), ], required=False, )
    prog_info_ids = fields.One2many(comodel_name="vessel.programme", inverse_name="daughter_id",
                                    string="Programme Information", required=False, )


class VesselProgramme(models.Model):
    _name = 'vessel.programme'
    _rec_name = 'programme_id'
    _description = 'Vessel Programme Information'

    programme_id = fields.Char(string="Program Identification", default=lambda self: _('New'), requires=False,
                               readonly=True, trace_visibility='onchange',)
    mother_id = fields.Many2one(comodel_name="vessel.vessel", string="Mother Vessel", required=False, )
    daughter_id = fields.Many2one(comodel_name="vessel.vessel", string="Daughter Vessel", required=False, )
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
                                          selection=[('active', 'Active'), ('expired', 'Expired'), ],
                                          required=False, default='active')
    navy_clear = fields.Date(string="Navy Clearance Date", required=False, )
    navy_clear_validity = fields.Integer(string="Clearance Validity", required=False,)
    navy_clear_expiry = fields.Date(string="Date of Expiry of Clearance", required=False)
    navy_clear_status = fields.Selection(string="Status of Reapplication",
                                         selection=[('active', 'Active'), ('expired', 'Expired'), ],
                                         required=False, default='active')
    dpr_clear = fields.Date(string="DPR Clearance", required=False,)
    sts_hose_connection = fields.Datetime(string="STS Hose Connection Time", required=False, )
    sts_start = fields.Datetime(string="STS Start", required=False,)
    sts_complete = fields.Datetime(string="STS Completion", required=False,)
    sts_hose_disconnection = fields.Datetime(string="STS Hose Disconnection", required=False)
    documentation_start = fields.Date(string="Documentation Start", required=False)
    documentation_complete = fields.Date(string="Documentation Completion", required=False)
    bl_mt = fields.Integer(string="B/L FIG MT", required=False,)
    bl_litre = fields.Integer(string="B/L FIG Litre", required=False, )
    bunker_receipt_start = fields.Datetime(string="Bunker Receipt Start", required=False,)
    bunker_receipt_complete = fields.Datetime(string="Bunker Receipt Completion", required=False, )
    armed_embarkation = fields.Datetime(string="Armed Guard Embarkation", required=False,)
    cast_off = fields.Datetime(string="Cast Off", required=False, )
    arrive_anchor = fields.Datetime(string="Arrived Anchorage", required=False, )
    berthing = fields.Datetime(string="Berthing", required=False, )
    pppra_clear = fields.Datetime(string="PPPRA Clearance Receipt", required=False, )
    discharge_commence = fields.Datetime(string="Discharge Commencement", required=False, )
    discharge_complete = fields.Datetime(string="Discharge Completion", required=False, )
    cast_off_berth = fields.Datetime(string="Cast Off from Berth", required=False, )
    arrive_lag_anchor = fields.Datetime(string="Arrived Lagos Anchorage", required=False, )
    voyage_duration = fields.Integer(string="Voyage Duration", required=False,)
    standard_duration = fields.Integer(string="Standard Voyage Duration", required=False, )
    voyage_duration_variance = fields.Integer(string="Variance in Voyage Duration", required=False, )
    remark = fields.Text(string="Remarks", required=False, )

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

