from flask import Flask,jsonify,request
from blockchain.Blockchain import Blockchain
from blockchain.Transaction import Transaction
app = Flask(__name__)

blockchain = Blockchain()



@app.route("/" , methods=['GET'])
def get_chain():
    try:
        chain_data = blockchain.get_dict()  # Certifique-se de que este método existe
        response = {
            'chain': chain_data,
            'length': len(blockchain.chain)
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/transactions/new", methods=['POST'])
def new_transaction():
    # t1 = Transaction("Carlos","Franch",500)
    values = request.get_json()
    required = ['sender','receiver','amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    transaction = Transaction(sender=values['sender'] , receiver=values['receiver'], amount=values['amount'])
    # myBC.add_block(t1,1)
    blockchain.add_block(transaction=transaction,proof=1)
    response = {'message': f"Transaction add to blockchain!"}
    return jsonify(response),201

if __name__ == '__main__':
    app.run()