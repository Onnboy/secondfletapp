import flet as ft

def main(page: ft.Page):
    page.title = "App de Lista de tarefas"
    
    task_list = ft.Column(spacing=10)
    task_count = ft.Text(value="Tarefas Pendentes: 0")
    search_field  = ft.TextField(hint_text="Buscar tarefas", expand=True, on_change=lambda e: search_tasks())
    
    input_field = ft.TextField(hint_text="Nova tarefa", expand=True)
    add_button = ft.ElevatedButton("Acrescentar", on_click=lambda e: add_task(e))
    
    def update_task_count():
        count = sum(1 for task in task_list.controls if not task.controls[0].value)
        task_count.value = f"Tarefas Pendentes: {count}"
        page.update()
        
    def add_task(e):
        task_text = input_field.value.strip()
        if task_text:
            task = ft.Row(
                [
                    ft.Checkbox(value=False, on_change=toggle_task_status),
                    ft.Text(task_text),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: confirm_delete(task)),
                ]
            )
            task_list.controls.append(task)
            input_field.value = ""
            update_task_count()
            page.update()
            
    def toggle_task_status(e):
        checkbox = e.control
        if checkbox.value:
            checkbox.parent.controls[1].style = ft.TextStyle(decoration="lineThrough")
        else:
            checkbox.parent.controls[1].style = None
            
        update_task_count()
        page.update()
            
    def confirm_delete(task):
        def on_confirm(e):
            task_list.controls.remove(task)
            update_task_count()
            dialog.open = False
            page.update()
            
        dialog = ft.AlertDialog(
            title=ft.Text("Confirmação"),
            content=ft.Text("Deseja realmente excluir esta tarefa?"),
            actions=[
                ft.TextButton("Sim", on_click=on_confirm),
                ft.TextButton("Não", on_click=lambda e: dialog.close()),
            ],
        )
        page.dialog = dialog
        dialog.open = True
        page.update()
    
    def search_tasks():
        query = search_field.value.lower()
        for task in task_list.controls:
            task.visible = query in task.controls[1].value.lower()
        page.update()
        
    def edit_task(e):
        task_text = e.control
        task_text.reandoly = False
        task_text.focus()
        page.update()
    
    page.add(
        ft.Column(
            [
                ft.Row([input_field, add_button], spacing=10),
                search_field,
                task_count,
                task_list
            ],
            alignment="center"
        )
    )
        
ft.app(target=main)