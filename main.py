from fasthtml.common import serve, Div, Span
from monsterui.all import H1, H2, Card, Button, Form, Input, ButtonT, Container, ContainerT, Theme, fast_app

app, rt = fast_app(hdrs=Theme.blue.headers())
counter = 0

@rt
def index():
    return Container(
        H1('🚀 Counter App', cls='text-3xl font-bold text-center mb-6 mt-6'),

        Card (cls='p-6 text-center mb-4')(
            H2('Click the buttons!', cls='mb-4'),
            Div(cls='flex items-center justify-center gap-4')(
                Button('-', hx_post='/dec', hx_target='#count')
            ),
            Span(id='count', cls='text-2xl font-bold')(counter),   
        )
    )

@rt('/inc', methods=['POST'])
def inc():
    global counter
    counter += 1
    return counter

@rt('/dec', methods=['POST'])
def dec():
    global counter
    counter -= 1
    return counter

@rt('/hello',methods=['POST'])
def hello(name:str):
    return f'Hello {name}!'