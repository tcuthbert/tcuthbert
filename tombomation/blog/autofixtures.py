from blog.models import Post, Category
from autofixture import generators, register, AutoFixture
import random

class PostAutoFixture(AutoFixture):
    field_values = {
        'content_markdown': generators.StaticGenerator("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
        'categories': ['cisco', 'python']
    }
    #generate_m2m = {'categories': (1,3)}

class CategoryAutoFixture(AutoFixture):
    class Values:
        #title = generators.ChoicesGenerator(
            #values=(('python', 'golang', 'cisco'))
        #)
        title = random.choice(
            ('python', 'golang', 'cisco')
        )

register(Post, PostAutoFixture)
register(Category, CategoryAutoFixture)
