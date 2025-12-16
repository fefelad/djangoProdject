from quart import Blueprint, abort, render_template, request, jsonify, send_from_directory, redirect

blueprint = Blueprint('oleg', __name__, 
                      template_folder="templates",
                      static_url_path='/static')

@blueprint.route('/', methods=["GET", "POST"])
async def main_page():
    ctx: dict = {"title": "Главная"}
    
    if request.method == "POST":
        form_data = await request.form
        
        # Определяем какая форма была отправлена
        if 'review-from' in form_data:
            print("=" * 50)
            print("ОТЗЫВ ОТПРАВЛЕН:")
            print(f"От кого: {form_data.get('review-from', 'Не указано')}")
            print(f"Оценка: {form_data.get('review-score', 'Не указано')}")
            print(f"Комментарий: {form_data.get('review-comment', 'Не указано')}")
            print("=" * 50)
            
        elif 'order-station' in form_data:
            print("=" * 50)
            print("ЗАКАЗ КОНЦЕРТА:")
            print(f"Станция метро: {form_data.get('order-station', 'Не указано')}")
            print(f"ФИО заказчика: {form_data.get('order-fio', 'Не указано')}")
            print("=" * 50)
    
    return await render_template("index.html", context=ctx)