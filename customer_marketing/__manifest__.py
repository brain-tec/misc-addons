# -*- coding: utf-8 -*-
{
    "name": """Customer Marketing""",
    "summary": """Allows to store detailed information about customers""",
    "category": "Marketing",
    # "live_test_URL": "",
    "images": ["static/description/icon.png"],
    "vesion": "10.0.1.0.0",
    "application": False,
    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@itpp.dev",
    "website": "https://it-projects.info",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["contacts"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/res_partner_views.xml"],
    "qweb": [],
    "demo": [],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
}
