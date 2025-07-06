import uuid

def generate_transaction_reference():
    return str(uuid.uuid4()).replace("-", "").upper()[:12]