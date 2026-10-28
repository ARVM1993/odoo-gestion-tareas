from odoo import models, fields


class GestionTarea(models.Model):
    _name = 'gestion.tarea'
    _description = 'Tarea'
    _order = 'fecha_limite asc, id desc'

    name = fields.Char(
        string='Nombre de la tarea',
        required=True
    )

    descripcion = fields.Text(
        string='Descripción'
    )

    fecha_limite = fields.Date(
        string='Fecha límite'
    )

    estado = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('proceso', 'En proceso'),
            ('completada', 'Completada'),
        ],
        string='Estado',
        default='pendiente',
        required=True
    )