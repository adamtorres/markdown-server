import os

ms_encoding = "utf-8"
ms_port = "8009"
ms_host = "0.0.0.0"
ms_debug = True
ms_reloader = True
html_extension = ".html"
root_path = os.path.dirname(__file__)
resource_dir = os.path.join(root_path, "resources")
markdown_dir = os.path.join(resource_dir, "markdown")
html_dir = os.path.join(resource_dir, "html")
css_dir = os.path.join(resource_dir, "css")
css_name = "combined.css"
css_path = os.path.join(css_dir, css_name)
markdown_type = ["mdx_gfm","markdown.extensions.toc","markdown.extensions.def_list", "markdown.extensions.codehilite", ]
