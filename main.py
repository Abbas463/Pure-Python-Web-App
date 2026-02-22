from fasthtml.common import serve, Div, Span
from monsterui.all import H1, H2, Card, Button, Form, Input, ButtonT, Container, ContainerT, Theme, fast_app

app, rt = fast_app(hdrs=Theme.blue.headers())
counter = 0

@rt
def index():
    return Container(
        
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