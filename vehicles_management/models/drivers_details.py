from odoo import models, fields, api


class DriversDetails(models.Model):
    _name="drivers.details"
    _description = "manage drivers Details"

    full_name = fields.Char(string="Driver Full Name", requirde=True)
    permanent_address = fields.Char(string="Permanent Address", requirde=True)
    driver_age = fields.Integer("Driver Age")
    driver_nic_number = fields.Integer("Driver NIC Number", requirde=True)
    driver_nic_image_upload = fields.Image("Driver NIC Image Upload", max_width=750, max_height=750,  requirde=True)
    driver_valid_driving_license_number = fields.Integer("Driver Valid Driving license number", requirde=True)
    driver_license_image_upload = fields.Image(" Driving License Image upload", max_width=750, max_height=750,  requirde=True)
    drive_license_expire_date = fields.Date("Drive License Expire Date")


    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    propic = fields.Image('Profile Pic', max_width=750, max_height=750)
    contact = fields.Char('Contact No')
    email = fields.Char('Email')
    address = fields.Char('Address')

