from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
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

        # 처리 -> Todo
        # 잔액 확인 수행

        # Signature 생성

        signature = ''

        json_data = {
            'send_public_key': '',
            'send_blockchain_addr': '',
            'recv_blockcahin_addr': '',
            'amount':10,
            'signature':signature, 
        }

        result ={
            'status':'success',
            'amount': data_dic.get('amount')
        }
        return jsonify(result)

    return render_template(
        'transfer.html',
        form = form,
    )