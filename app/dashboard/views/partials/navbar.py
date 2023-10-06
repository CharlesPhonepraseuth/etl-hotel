# Third party imports
import dash_bootstrap_components as dbc


def create_navbar():

    navbar = dbc.NavbarSimple(
        children = [
            dbc.DropdownMenu(
                nav = True,
                in_navbar = True,
                label = "Menu",
                children = [
                    dbc.DropdownMenuItem("Home", href = '/'),
                    dbc.DropdownMenuItem(divider = True),
                    dbc.DropdownMenuItem("Analysis", href = '/hotel-analysis')
                ],
            ),
        ],
        brand = "Dashboard",
        brand_href = "/",
        sticky = "top",
        color = "primary",
        dark = True
    )

    return navbar
