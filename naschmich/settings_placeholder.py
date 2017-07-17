def get_placeholder_settings():
    placeholders = {
        'contact.html map': {
            "plugins": ['FilerImagePlugin', 'GoogleMapPlugin']
        },
        'contact.html contact': {
            "plugins": [''],
            'text_only_plugins': ['LinkPlugin'],
            "limits": {
                'LinkPlugin': 1
            },
            "child_classes": {
                'LinkPlugin': [''],
            }
        },
        'contact.html contact_details': {
            "plugins": ['TextPlugin'],
            "limits": {
                'TextPlugin': 1
            },
        },
        'gallery.html content': {
            "plugins": ['Gallery4Plugin', 'Gallery6Plugin', 'Gallery8Plugin']
        },
        'aside_links': {
            "plugins": ['LinkPlugin'],
            "child_classes": {
                'LinkPlugin': [''],
            }
        },
        'about': {
            "plugins": [''],
            'text_only_plugins': ['LinkPlugin'],
            "limits": {
                'LinkPlugin': 1
            },
            "child_classes": {
                'LinkPlugin': [''],
            }
        },
        'gallery': {
            "plugins": [''],
            'text_only_plugins': ['LinkPlugin'],
            "limits": {
                'LinkPlugin': 1
            },
            "child_classes": {
                'LinkPlugin': [''],
            }
        },
        'impressum': {
            "plugins": [''],
            'text_only_plugins': ['LinkPlugin'],
            "limits": {
                'LinkPlugin': 1
            },
            "child_classes": {
                'LinkPlugin': [''],
            }
        },
        'logo': {
            "plugins": [''],
            "limits": {
                'FilerImagePlugin': 1
            },
        },
    }
    return placeholders
