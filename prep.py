from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        job = 0
    else:
        job = 1
    return render_template('training.html', job=job)

@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    list_prof = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')
    return render_template('list_prof.html', list_prof=list_prof, list_type=list_type)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
