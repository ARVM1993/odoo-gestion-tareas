{
    'name': 'Gestión de Tareas',
    'version': '17.0.1.0.0',
    'summary': 'Módulo sencillo para gestionar tareas',
    'category': 'Productivity',
    'author': 'Personalizado',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/tarea_views.xml',
    ],
    'installable': True,
    'application': True,
}