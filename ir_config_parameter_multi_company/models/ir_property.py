from odoo import api, models


class IrProperty(models.Model):
    _inherit = "ir.property"

    @api.multi
    def write(self, vals):
        res = super(IrProperty, self).write(vals)
        field = self.env.ref("base.field_ir_config_parameter_value")
        self._update_db_value_website_dependent(field)
        return res
