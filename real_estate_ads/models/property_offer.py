from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError

class PropertyOffer(models.Model):
    _name = 'estate.property.offer'   #name of model
    _description = 'Estate Property Offers'

    price = fields.Float(string="Price")
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        string="Status"
    )
    property_id = fields.Many2one('estate.property', string="Property")
    partner_id = fields.Many2one('res.partner', string="Partner")
    @api.model
    def _set_create_date(self):
        return fields.Date.today()

    creation_date = fields.Date(string="Create Date", default=_set_create_date)
    validity = fields.Integer(string="Validity")

    #takes fields as arguments, that field is in view and also included in create or write call
    #validity cant be negative.
    # @api.constrains('validity')
    # def _check_validity(self):
    #     for rec in self:
    #         if rec.validity < 0:
    #             raise ValidationError("Validity cannot be negative")

    _sql_constraints = [
        ('check_validity', 'check(validity > 0)', 'Validity must be positive')
    ]

    @api.depends('creation_date', 'validity')
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False
    def _inverse_deadline(self):
        for rec in self:
            if rec.deadline and rec.creation_date:
                rec.validity = (rec.deadline - rec.creation_date).days
            else:
                rec.validity = False
    deadline = fields.Date(string="Deadline", compute=_compute_deadline, inverse=_inverse_deadline)

    @api.model_create_multi  #to create multiple records
    def create(self, vals):  #here vals is record, create means first time adding
        for rec in vals:
            if not rec.get('creation_date'):
                rec['creation_date'] = fields.Date.today()
        return super(PropertyOffer, self).create(vals)

    def write(self, vals):   #vals are fields that are being updated
        print(vals)  #show whichever fields are updated
        res_partner_ids = self.env['res.partner']
        print(res_partner_ids, res_partner_ids.name)
        print(self)
        print(self.env)
        print(self.env.cr)
        print(self.env.uid)
        print(self.env.context)
        return super(PropertyOffer, self).write(vals)

    def unlink(self):
        return super(PropertyOffer,self).unlink()


    @api.autovacuum
    def _clean_offers(self):
        self.search([('status', '=', 'refused')]).unlink()











