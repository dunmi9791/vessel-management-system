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

    programme_id = fields.Char()

