from odoo import fields, models, api

class Property(models.Model):
    _name = 'estate.property'    #name of model
    _description = 'Estate Properties'
    # fields
    name = fields.Char(string="Name", required=True)
    state = fields.Selection([('new', 'New'), ('old', 'Old')], string="State")
    def action_new(self):
        self.state = 'new'
    def action_old(self):
        self.state = 'old'
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
    type_id = fields.Many2one('estate.property.type', string="Property Type")
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")

    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    data_availability = fields.Date(string="Available From", readonly=True)
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Name")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('west', 'West'), ('east', 'East')],
        string="Garden Orientation")
    # @api.depends('living_area', 'garden_area')
    # def _depends_total_area(self):
    #     for rec in self:
    #         rec.total_area = rec.living_area + rec.garden_area

    @api.onchange('living_area', 'garden_area')
    def _onchange_total_area(self):
        self.total_area = self.living_area + self.garden_area

    total_area = fields.Integer(string="Total Area")
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer", domain=[('is_company', '=', True)])
    phone = fields.Char(string="Phone", related='buyer_id.phone')


    #access rights - id, create_date, create_uid, write_date, write_uid

class PropertyType(models.Model):
    _name = 'estate.property.type'   #name of model
    _description = 'Property Type'

    name = fields.Char(string="Name", required=True)

class PropertyTag(models.Model):
    _name = 'estate.property.tag'   #name of model
    _description = 'Property Tag'
    name = fields.Char(string="Name", required=True)



