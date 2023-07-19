import flet as ft
import eigen as eg


def main(page: ft.Page):
    page.title = "Engineering Mathematics Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    math1 = ft.ElevatedButton(text="Math-1",width=300, height=100)
    math2 = ft.ElevatedButton(text="Math-2",width=300, height=100)
    math3 = ft.ElevatedButton(text="Math-3",width=300, height=100)
    math4 = ft.ElevatedButton(text="Math-4",width=300, height=100)

    row_1 = ft.Row(controls=[math1, math2], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    row_2 = ft.Row(controls=[math3, math4], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    row_between = ft.Row()

    page.add(row_1, row_between, row_2)


ft.app(target=main)
