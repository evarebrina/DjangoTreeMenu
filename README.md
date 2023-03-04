# TreeMenu - tree menu django app

This project contains tree_menu app with tree menu feature implemented 
with template tag. Menus and items can be managed through
Django admin interface, then menu can be printed on any page with tag `{% draw_menu 'menu_slug %}`.
The project contains `example_items.json` file with sample data
that can be loaded to database for demonstration purpose.

### Example usage
0. Install requirements

`pip install -r requirements.txt`

1. Create migration file and run it on database

`python manage.py makemigrations`

`python manage.py migrate`

2. Load sample data to db

`python manage.py loaddata example_items.json`

3. Run a server

`python manage.py runserver`

4. Go to `127.0.0.1:8000`

Additionally new menus and menu items can be added/edited/deleted
through Django admin page. To do that, first create a superuser with 
`python manage.py createsuperuser` and log in to admin panel. There you can
add new menus on Menu page and then draw them by adding `{% draw_menu 'menu_slug %}` to
`templates/home.html` file. In order for menu to have items in it add MenuItem objects
related to this menu. Any MenuItem must have either url or named url to be added.
An active menu item is determined based on URL if current page. Path to active item and
the first level after active item are unfolded. If you click in item you goу