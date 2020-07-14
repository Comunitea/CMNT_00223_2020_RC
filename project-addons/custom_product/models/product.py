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


class ProductTemplate(models.Model):
    _inherit = "product.template"

    uses = fields.Text('Product Uses')
    references = fields.Text('References')

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100,
                     name_get_uid=None):
        print("NAME SEARCH")
        res = super()._name_search(
            name, args=args, operator=operator, limit=limit,
            name_get_uid=name_get_uid)
        print(name)
        if name:
            tmpl_product_ids = self._search(
                ['|', '|', ('uses', operator, name),
                ('references', operator, name),
                ('description', operator, name)], limit=limit,
                access_rights_uid=name_get_uid)
            print(tmpl_product_ids)
            res.extend(self.browse(tmpl_product_ids).name_get())
        return res


class ProductProduct(models.Model):
    _inherit = "product.product"

    
    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100,
                     name_get_uid=None):
        print("NAME SEARCH")
        res = super()._name_search(
            name, args=args, operator=operator, limit=limit,
            name_get_uid=name_get_uid)
        print(name)
        if name:
            product_ids = self._search(
                ['|', '|', ('uses', operator, name),
                ('references', operator, name),
                ('description', operator, name)], limit=limit,
                access_rights_uid=name_get_uid)
            print(product_ids)
            res.extend(self.browse(product_ids).name_get())
        return res