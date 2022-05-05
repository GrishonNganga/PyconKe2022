import json
from web3 import Web3

network_url= "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(network_url))
contract_address = ""
contract_abi = ''

def create_account(private_key = None):
    if private_key:
        acct = web3.eth.account.privateKeyToAccount(private_key)
        print(acct)
        return acct.address
    else:
        account = web3.eth.account.create()
        return account.address, web3.toHex(account.privateKey)

def send_eth(to_account, amount):
    from_account = web3.eth.accounts[0]

    tx = {
        "nonce": web3.eth.get_transaction_count(from_account),
        "to": to_account,
        "value": web3.toWei(amount, "ether"),
        "gas": 2000000,
        "gasPrice": web3.toWei(50, "gwei")
    }

    signed_tx = web3.eth.account.sign_transaction(tx, "ea34a23473fa895af810ec354474fef923686007242f510883a18d93028a04d6")

    try:
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_response = web3.eth.get_transaction_receipt(tx_hash)

        if tx_response and tx_response["status"] == 1:
            return True, None
        else:
            return False, "Something wrong happened"

    except Exception as e: 
        return False, e["message"]
    
def format_address(address):
    return web3.toChecksumAddress(address)