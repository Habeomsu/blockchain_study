from flask import (
    Blueprint,
    render_template,
    request,
)
from wallet.forms import TransferForm

bp = Blueprint('transfer', __name__, url_prefix='/trans')

@bp.route('/transfer', methods=['GET','POST'])
def transfer():
    '''코인 지갑 화면'''
    form = TransferForm()

    if request.method=='POST' and form.validate_on_submit():
        data_dic = request.form.to_dict()
        print(f'data_dic: { data_dic}')

    return render_template(
        'transfer.html',
        form = form,
    )