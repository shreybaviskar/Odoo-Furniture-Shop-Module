from odoo import models, fields, api

class FurnitureAppointment(models.Model):
    _name = 'furniture.appointment'
    _description = 'Customer Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', required=True, copy=False,
                       readonly=True, default='New')
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    date = fields.Datetime(string='Appointment Date', default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ], string='Status', default='draft', tracking=True)
    note = fields.Text(string='Internal Notes')
    email = fields.Char(related='customer_id.email', string="Email", readonly=True)
    phone = fields.Char(related='customer_id.phone', string="Phone", readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('furniture.appointment') or 'New'
        return super().create(vals_list)

    def action_confirm(self):
        for record in self:
            record.state = 'confirmed'

    def action_ongoing(self):
        for record in self:
            record.state = 'ongoing'

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_cancel(self):
        for record in self:
            record.state = 'canceled'