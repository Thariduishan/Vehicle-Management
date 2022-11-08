from odoo import models, fields, api
from datetime import date, datetime


class VehiclesDetails(models.Model):
    _name = "vehicles.details"
    _description = "manage vehicles Details"

    vehicle_reg_number = fields.Char(string="Vehicle Reg Number", requirde=True)
    vehicle_reg_date = fields.Date(string="Vehicle Reg Date", default=fields.Date.today,)
    Vehicle_owner_name = fields.Char(srring="Vehicle Owner Name", requirde=True)
    Vehicle_owner_mobile_number = fields.Integer(srring="Vehicle Owner Mobile Number", requirde=True)
    Vehicle_owner_nic_number = fields.Char(srring="Vehicle Owner NIC Number", requirde=True)
    vehicle_owner_nic_image_upload = fields.Image("Vehicle Owner NIC Image Upload", max_width=750, max_height=750,
                                                  requirde=True)
    vehicle_valid_insurance_number = fields.Integer("Vehicle Valid Insurance Number")

    vehicle_valid_insurance_image_upload = fields.Image("Vehicle Valid Insurance Image Upload", max_width=750,
                                                        max_height=750, requirde=True)
    vehicle_valid_revenue_license_number = fields.Integer(srring="Vehicle Valid Revenue License Number")
    vehicle_revenue_license_image_upload = fields.Image(srring="Vehicle Revenue License Image upload", max_width=750,
                                                        max_height=750, requirde=True)
    vehicle_insurance_next_expiry_date = fields.Char(string="Vehicle Insurance Next Expiry Date")
    vehicle_revenue_license_next_expiry_date = fields.Date("Vehicle Revenue License Next Expiry Date")

    vehicle_availability = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Vehicle Availability')
