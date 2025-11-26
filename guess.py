from flask import Flask, render_template
import random
from functools import wraps
app = Flask(__name__)

     
           
@app.route("/")
def home():
    return render_template('index.html')


sg_number = random.randint(1,10)
print(sg_number)


def make_bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b> {func(*args, **kwargs)} </b>"
    return wrapper


@app.route('/<int:your_num>')
@make_bold
def yourNum(your_num):
    if your_num < sg_number:
        
        return '''
                <h1 style='color:orange; text-align:center'> 
                        You Choose small Number 
                </h1>
                <div style="text-align:center">
                    <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2NlNTlxZ3lxbXJ2amZuMmFxNnE1ajQzaGQxaTQyMWQ0ajY5OHk5MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JT7Td5xRqkvHQvTdEu/giphy.gif" style="height:120px; width:120px;">
                </div>
            '''
            
    elif your_num > sg_number:
        return '''
                <h1 style='color:orange; text-align:center'>You Choose large Number</h1>
                <div style="text-align:center">
                    <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2NlNTlxZ3lxbXJ2amZuMmFxNnE1ajQzaGQxaTQyMWQ0ajY5OHk5MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JT7Td5xRqkvHQvTdEu/giphy.gif" style="height:120px; width:120px;">
                </div>
               ''' 
    else:
        return '''
                <h1 style='color:green; text-align:center'>You choose correct number</h1>
                <div style="text-align:center">
                    <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOG4xNGF4ZzdsYjQxdnN0ZWI2dmpyengzNTl3M2o1YTZtZnBwNDR1ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KBxyo8FDKE33qnj3KB/giphy.gif" style="height:120px; width:120px;">
                </div>
                '''
        


if __name__ == "__main__":
    app.run(debug = True) 
