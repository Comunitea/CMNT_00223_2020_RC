# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2020 Comunitea Servicios Tecnológicos S.L. All Rights Reserved
#    Vicente Ángel Gutiérrez Fernández <vicente@comunitea.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models, _
from odoo.osv.expression import get_unaccent_wrapper
import re

class CrmLead(models.Model):
    _inherit = "crm.lead"

    partner_ref = fields.Char(string="Partner Reference", related="partner_id.ref")    
    partner_category_id = fields.Many2many('res.partner.category', column1='partner_id',
                                    column2='category_id', string='Partner Tags', related="partner_id.category_id")
    partner_image_small = fields.Binary(related="partner_id.image_small")
    partner_parent_id = fields.Many2one('res.partner', string='Related Company', related="partner_id.parent_id")
    partner_is_company = fields.Boolean(string='Is a Company', related="partner_id.is_company")
    partner_type = fields.Selection(related="partner_id.type")
    partner_display_name = fields.Char(related="partner_id.display_name")