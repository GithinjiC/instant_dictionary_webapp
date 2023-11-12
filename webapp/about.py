import justpy as jp
from . import layout
# from . import page


class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the About page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
                At vero eos et accusamus et iusto odio dignissimos ducimus 
                qui blanditiis praesentium voluptatum deleniti atque corrupti 
                quos dolores et quas molestias excepturi sint occaecati 
                cupiditate non provident, similique sunt in culpa qui 
                officia deserunt mollitia animi, id est laborum et 
                dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. 
                Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod 
                maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. 
                Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus 
                saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. 
                Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores 
                alias consequatur aut perferendis doloribus asperiores repellat.
        """, classes="text-lg")
        return wp


# jp.Route(About.path, About.serve)
# jp.justpy(port=8001)
