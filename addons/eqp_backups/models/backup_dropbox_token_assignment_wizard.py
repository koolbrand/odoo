from odoo import models, fields

class BackupDropboxTokenAssignmentWizard(models.TransientModel):
    _name = 'backup.dropbox.token.assignment.wizard'
    _description = 'Dropbox Token Assignment Wizard'

    dropbox_auth_url = fields.Char(string="Authorization URL")
    dropbox_auth_code = fields.Char(string="Authorization Code")
    server_id = fields.Many2one('backup.server', string="Backup Server")
