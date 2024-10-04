from flet import *


menubar=AppBar(
    title=Text("For Trainning 4T",size=25,color=colors.WHITE),
    bgcolor=colors.AMBER,
    center_title=True,
    actions=[
        IconButton(icons.LOGIN,icon_color=colors.WHITE),
        IconButton(icons.HOME,icon_color=colors.WHITE),
        PopupMenuButton(
            items=[
                PopupMenuItem(text="Contact"),
                PopupMenuItem(text="about us"),
                PopupMenuItem(text="create account")
            ],
            
        )
    ]
)
