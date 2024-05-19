from odoo import fields, models

class Info(models.Model):
    _name = 'device.info'  # name of model
    _description = 'All devices'

    # fields
    device_id = fields.Integer(string="Id")
    name = fields.Char(string="Name", required=True)
    device_type = fields.Char(string="Device Type", required=True)

class DeviceIssue(models.Model):
    _name = 'device.issue'  # name of model
    _description = 'Issue of Devices'

    # fields
    device_id = fields.Integer(string="Device Id")
    name = fields.Char(string="Name", required=True)
    emp_id = fields.Many2one('hr.employee', string="Employee")
    start_date = fields.Date(string="Start Date")
    _sql_constraints = [
        ('unique_device_id', 'UNIQUE(device_id)', 'Device ID must be unique!'),
    ]

class DeviceComplaint(models.Model):
    _name = 'device.complaint'  # name of model
    _description = 'Complaints for Issued Devices'

    # fields
    emp_id = fields.Integer(string="Employee Id")
    device_id = fields.Integer(string="Device Id")
    reason = fields.Text(string="Reason", required=True)
    user = fields.Many2one('res.users', string="User")
    if_approved = fields.Boolean(string="Approved by User", default=False)

    def action_replace_device(self):
        replace_data = {
        'emp_id':self.emp_id,
        'device_id':self.device_id,
        'user':self.user.name,
        'reason':self.reason,
        'date':fields.Date.today()
        }
        self.env['device.replacement'].create(replace_data)


class DeviceReplacement(models.Model):
    _name = 'device.replacement'  # name of model
    _description = 'Replacement of Issued Devices'

    # fields
    emp_id = fields.Integer(string="Employee Id")
    device_id = fields.Integer(string="Old Device Id")
    user = fields.Text(string="Approved By")
    reason = fields.Text(string="Reason", required=True)
    date = fields.Date(string="Date of Replacement")
