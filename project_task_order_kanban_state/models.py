from odoo import api, fields, models


class ProjectTaskOrder(models.Model):
    _inherit = "project.task"

    kanban_state_num = fields.Integer(
        "Kanban state num", compute="_compute_kanban_state_num", store=True
    )

    @api.depends("kanban_state")
    def _compute_kanban_state_num(self):
        for r in self:
            if r.kanban_state == "normal":
                r.kanban_state_num = 0
            elif r.kanban_state == "done":
                r.kanban_state_num = 1
            else:
                r.kanban_state_num = 2

    _order = "kanban_state_num, priority desc, sequence, date_start, name, id"
