from flask import Flask, jsonify ,json,request ,send_file
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
from fpdf import FPDF

app = Flask(__name__)
CORS(app)
# set up the MongoDB client
#client = MongoClient("mongodb+srv://kreifeur:brahim2000@cluster0.vuhlwgu.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient("mongodb+srv://brahimkreifeur:brahim2000@cluster0.jwwjhmz.mongodb.net/?retryWrites=true&w=majority")
# select the database
db = client["Goujil"]

# select the collections
products = db["products"]
customers = db["customers"]
suppliers = db['suppliers']
purchases =db['purchases']
ventes =db['ventes']
achats =db['achats']
charges =db['charges']


# perform database operations
# for example, insert a document

@app.route("/")
def index():
    return 'flask'

@app.route("/products")
def get_products():
    data = []
    for document in products.find():
        data.append({
            'ref':document['ref'],
            'id': str(document['_id']),
            "name": document["name"],
            "price1": document["price1"],
            "price2": document["price2"],
            "price3": document["price3"],
            'qte':document['qte'],
            'date':document['date'],
        })
    return jsonify(data)


@app.route("/product/<name>")
def get_product(name):
    data = []
    for document in products.find({'name':name}):
        data.append({
            'id': str(document['_id']),
            "name": document["name"],
            "price1": document["price1"],
            "price2": document["price2"],
            "price3": document["price3"],
            'qte':document['qte'],
            'date':document['date'],
        })
    return jsonify(data) 

@app.route("/addproduct",methods=['POST'])
def add_product():
    ref = request.json['ref']
    name = request.json['name']
    price1=request.json['price1']
    price2=request.json['price2']
    price3=request.json['price3']
    qte=request.json['qte']
    date= request.json['date']
    products.insert_one({'ref':ref,'name': name ,'price1': price1 ,'price2': price2 ,'price3': price3 ,'qte': qte ,'date': date })
    return {'msg':'added'}


@app.route("/<id>", methods=["DELETE"])
def delete_product(id):
    result = products.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return "", 404
    return "", 204

@app.route("/<id>", methods=["PUT"])
def update(id):
    name = request.json["name"]
    price1 = request.json["price1"]
    price2 = request.json["price2"]
    price3 = request.json["price3"]
    qte = request.json["qte"]
    date = request.json["date"]
    result = products.update_one({"_id": ObjectId(id)}, {"$set": {"name": name, "price1": price1,"price2": price2,"price3": price3,'qte':qte,'date':date}})
    if result.modified_count == 0:
        return "", 404
    return "", 204

#------------------------------------- suppliers------------------------------------------------------
@app.route("/suppliers")
def get_suppliers():
    data = []
    for document in suppliers.find():
        data.append({
            'id': str(document['_id']),
            'ref': document['ref'],
            "name": document["name"],
            "phone": document["phone"],
            "productslist": document["productslist"],
            'adress': document['adress'],
            'taamol':document['taamol'],
            'gain':document['gain'],
        })
    return jsonify(data)



@app.route("/supplier/<name>")
def get_supplier(name):
    data = []
    for document in suppliers.find({'name':name}):
        data.append({
            'id': str(document['_id']),
            'ref': document['ref'],
            "name": document["name"],
            "phone": document["phone"],
            "productslist": document["productslist"],
            'adress': document['adress'],
            'taamol':document['taamol'],
            'gain':document['gain'],
        })
    return jsonify(data)

@app.route("/addsupplier",methods=['POST'])
def add_supplier():
    name = request.json['name']
    ref = request.json['ref']
    phone=request.json['phone']
    productslist=request.json['productslist']
    taamol= request.json['taamol']
    adress= request.json['adress']
    gain= request.json['gain']
    suppliers.insert_one({'ref':ref,'adress':adress,'taamol':taamol,'name': name ,'phone': phone ,'productslist': productslist ,'gain':gain})
    return {'msg':'added'}


@app.route("/supplier/<id>", methods=["DELETE"])
def delete_supplier(id):
    result = suppliers.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return "", 404
    return "", 204

@app.route("/supplier/<id>", methods=["PUT"])
def update_supplier(id):
    name = request.json['name']
    ref = request.json['ref']
    phone=request.json['phone']
    productslist=request.json['productslist']
    taamol= request.json['taamol']
    adress= request.json['adress']
    gain= request.json['gain']
    result = suppliers.update_one({"_id": ObjectId(id)}, {"$set": {'ref':ref,'adress':adress,'taamol':taamol,'name': name ,'phone': phone ,'productslist': productslist ,'gain':gain}})
    if result.modified_count == 0:
        return "", 404
    return "", 204

#------------------------------------- customers------------------------------------------------------
@app.route("/customers")
def get_customers():
    data = []
    for document in customers.find():
        data.append({
            'id': str(document['_id']),
            'ref': document['ref'],
            "name": document["name"],
            "phone": document["phone"],
            "productslist": document["productslist"],
            'adress': document['adress'],
            'taamol':document['taamol'],
            'gain':document['gain'],
        })
    return jsonify(data)

@app.route("/customer/<name>")
def get_customer(name):
    data = []
    for document in customers.find({'name':name}):
        data.append({
            'id': str(document['_id']),
            'ref': document['ref'],
            "name": document["name"],
            "phone": document["phone"],
            "productslist": document["productslist"],
            'adress': document['adress'],
            'taamol':document['taamol'],
            'gain':document['gain'],
        })
    return jsonify(data)

@app.route("/addcustomer",methods=['POST'])
def add_customer():
    name = request.json['name']
    ref = request.json['ref']
    phone=request.json['phone']
    productslist=request.json['productslist']
    taamol= request.json['taamol']
    adress= request.json['adress']
    gain= request.json['gain']
    customers.insert_one({'ref':ref,'adress':adress,'taamol':taamol,'name': name ,'phone': phone ,'productslist': productslist ,'gain':gain})
    return {'msg':'added'}


@app.route("/customer/<id>", methods=["DELETE"])
def delete_customer(id):
    result = customers.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return "", 404
    return "", 204

@app.route("/customer/<id>", methods=["PUT"])
def update_customer(id):
    name = request.json['name']
    ref = request.json['ref']
    phone=request.json['phone']
    productslist=request.json['productslist']
    taamol= request.json['taamol']
    adress= request.json['adress']
    gain= request.json['gain']
    result = customers.update_one({"_id": ObjectId(id)}, {"$set": {'ref':ref,'adress':adress,'taamol':taamol,'name': name ,'phone': phone ,'productslist': productslist ,'gain':gain}})
    if result.modified_count == 0:
        return "", 404
    return "", 204
#------------------------------------- purchases------------------------------------------------------
@app.route("/purchases",methods=['GET'])
def get_purchases():
    data = []
    for document in purchases.find():
        data.append({
            'id': str(document['_id']),
            "name": document["customerId"],
            "total": document["total"],
            "achats": document["achats"],
        })
    return jsonify(data)


@app.route("/addpurchases",methods=['POST'])
def add_purchases():
    id = request.json['customerId']
    total=request.json['total']
    achats=request.json['achats']
    purchases.insert_one({'customerId': id ,'total': total ,'achats':achats})
    return {'msg':'added'}


#------------------------------------ventes :----------------------------------------------------
@app.route("/ventes")
def get_ventes():
    data = []
    for document in ventes.find():
        data.append({
            'id': str(document['_id']),
            'vendeur': document['vendeur'],
            "client": document["client"],
            "total": document["total"],
            "versement": document["versement"],
            'diff': document['diff'],
        })
    return jsonify(data)


@app.route("/addvente",methods=['POST'])
def add_vente():
    vendeur = request.json['vendeur']
    client = request.json['client']
    total=request.json['total']
    versement=request.json['versement']
    diff=request.json['diff']
    total_benefit= request.json['total_benefit']
    ventes.insert_one({'vendeur':vendeur,'client': client ,'total': total ,'versement': versement ,'diff': diff ,'total_benefit':total_benefit})
    return {'msg':'added'}


#------------------------------------achats :----------------------------------------------------
@app.route("/achats")
def get_achats():
    data = []
    for document in achats.find():
        data.append({
            'id': str(document['_id']),
            'fournisseur': document['fournisseur'],
            "total": document["total"],
            "versement": document["versement"],
            'diff': document['diff'],
        })
    return jsonify(data)


@app.route("/addachat",methods=['POST'])
def add_achat():
    fournisseur = request.json['fournisseur']
    total=request.json['total']
    versement=request.json['versement']
    diff=request.json['diff']
    achats.insert_one({'fournisseur': fournisseur ,'total': total ,'versement': versement ,'diff': diff })
    return {'msg':'added'}

#------------------------------------- somme de produit ------------------------------------------------------
@app.route("/CA")
def get_CA():
    CA = 0
    numberofproducts = 0
    credit_clients =0
    credit_over_clients=0
    credit_supp =0
    credit_over_supp =0
    total_versement=0
    total_achats=0
    benifits=0
    for document in products.find():
        # Convert the price and quantity to integers before calculating the total revenue
        try:
            price = int(document["price1"])
        except:
            price =int(document["price1"][0])
        quantity = int(document["qte"])
        CA += price * quantity
        numberofproducts += 1

    for document in customers.find():
        if int(document["gain"])>0:
            credit_clients += int(document["gain"])
        else:
            credit_over_clients += int(document["gain"])

    for document in suppliers.find():
        if int(document["gain"])>0:
            credit_supp += int(document["gain"])
        else:
            credit_over_supp += int(document["gain"])

    for document in ventes.find():
        total_versement += int(document["versement"])
        benifits += int(document['total_benefit'])

    for document in achats.find():
        total_achats += int(document["versement"])  

    data = {'CA': CA, 'numberofproducts': numberofproducts,
            'credit_clients':credit_clients ,
            'credit_over_clients':credit_over_clients,
            'credit_supp':credit_supp ,
            'credit_over_supp':credit_over_supp ,
            'total_versement':total_versement,
            'total_achats':total_achats,
            'benifits':benifits}
    return jsonify(data)

#------------------------------------- charge ------------------------------------------------------
@app.route("/charges")
def get_charges():
    data = []
    for document in charges.find():
        data.append({
            'id': str(document['_id']),
            "camion": document["camion"],
            "produit": document["produit"],
            "qte": document["qte"],
            'qterestant': document["qterestant"],
            'qteacheter': document["qteacheter"]
        })
    return jsonify(data)


@app.route("/charge/<name>/<camion>")
def get_charge(name,camion):
    data = []
    for document in charges.find({'produit':name,'camion':camion}):
        data.append({
            'id': str(document['_id']),
            "camion": document["camion"],
            "produit": document["produit"],
            "qte": document["qte"],
            'qterestant': document["qterestant"],
            'qteacheter': document["qteacheter"]
        })
    return jsonify(data) 



@app.route("/charge/<camion>")
def get_charge_by_camion(camion):
    data = []
    for document in charges.find({'camion':camion}):
        data.append({
            'id': str(document['_id']),
            "camion": document["camion"],
            "produit": document["produit"],
            "qte": document["qte"],
            'qterestant': document["qterestant"],
            'qteacheter': document["qteacheter"]
        })
    return jsonify(data) 

@app.route("/addcharge",methods=['POST'])
def addcharge():
    camion = request.json['camion']
    produit = request.json['produit']
    qte=request.json['qte']
    qteacheter=0
    qterestant=request.json['qte']
    charges.insert_one({'camion':camion,'produit':produit,'qte':qte,'qteacheter':qteacheter,'qterestant':qterestant})
    return {'msg':'added'}


@app.route("/charge/<id>", methods=["DELETE"])
def delete_charge(id):
    result = charges.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return "", 404
    return "", 204 

@app.route("/charge/<id>", methods=["PUT"])
def update_charge(id):
    camion = request.json['camion']
    produit = request.json['produit']
    qte=request.json['qte']
    qteacheter=request.json['qteacheter']
    qterestant=request.json['qterestant']
    result = charges.update_one({"_id": ObjectId(id)}, {"$set": {'camion':camion,'produit':produit,'qte':qte,'qteacheter':qteacheter,'qterestant':qterestant}})
    if result.modified_count == 0:
        return "", 404
    return "", 204 




#------------------------------------- Facture -------------------------------------------------------

def generate_receipt_to_pdf(products, client, vendeur, versement):
    pdf = FPDF()
    pdf.add_page()

    # Set font and size for the main content
    pdf.set_font("Arial", size=12)

    # Generate the receipt content
    receipt = "---------------------- RECEIPT----------------------\n"
    receipt += f"VENDEUR: {vendeur}\n"
    receipt += f"Client: {client}\n\n"
    total_amount = 0

    # Set font and size for product details
    pdf.set_font("Arial", size=10)

    for product in products:
        product_name = product['name']
        price = product['price3']
        quantity = product['qte2']
        product_total_amount = int(price) * int(quantity)
        receipt += "------------------------------------\n"
        receipt += f"Produit: {product_name}\n"
        receipt += f"Prix: {price}\n"
        receipt += f"Quant: {quantity}\n"
        receipt += f"Total: {product_total_amount}\n\n"

        total_amount += product_total_amount

    # Set font and size for total and payment details
    pdf.set_font("Arial", size=12, style='B')

    receipt += "----------------- TOTAL -------------------\n"
    receipt += f"Total: {total_amount}\n"
    receipt += f"----------------- Versement -------------------\n"
    receipt += f"Payment: {versement}\n"
    receipt += f"----------------- Difference -------------------\n"
    receipt += f"Difference: {total_amount - int(versement)}\n"
    receipt += "-------------------------------------------------\n\n"
    receipt += "Thank you for your purchase!"

    # Set font and size for footer
    pdf.set_font("Arial", size=8, style='I')

    # Write the receipt content to the PDF
    pdf.multi_cell(0, 10, txt=receipt)

    # Save the PDF to a temporary file
    pdf_file = 'receipt.pdf'
    pdf.output(pdf_file)

    return pdf_file

@app.route("/facture",methods=['POST'])
def make_facture():
    data = request.json['products']
    total = request.json['total']
    client = request.json['client']
    vendeur = request.json['vendeur']
    versement = request.json['versement']
    
    # Generate the receipt in PDF format and get the PDF file path
    pdf_file = generate_receipt_to_pdf(data, client, vendeur, versement)

    # Serve the PDF file for download
    return send_file(pdf_file, as_attachment=True)

if __name__ == "__main__":
    app.run(port=5000 , debug=True)
