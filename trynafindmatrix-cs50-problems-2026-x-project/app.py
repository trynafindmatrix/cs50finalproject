import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.utils import secure_filename

from helpers import login_required, admin_required, apology

app = Flask(__name__)


UPLOAD_FOLDER = 'static/items_img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# making a random key for admin
app.secret_key = "665521dbd8f9568a0e410fe3ff9f736c"

db = SQL("sqlite:///data.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# for my landing page which consists the about section
@app.route("/")
def homepage():
    return render_template("homepage.html")

#for my e-commerce index page or homepage which is accesible through homepage
@app.route("/index")
def index():

    items = db.execute("select * from items")

    if items:
        return render_template("index.html", items=items)
    else:
        return apology("empty store", "400")


@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    user_id = session["user_id"]

    if request.method == "POST":
        item_id = request.form.get("item_id")
        quantity = request.form.get("quantity")

        if not item_id or not quantity:
            return apology("invalid cart request item data selection", 400)

        try:
            quantity = int(quantity)
            if quantity <=0:
                return apology("invalid, quantity", 400)
            item_id = int(item_id)
        except ValueError:
            return apology("invalid dynamic selection unit count quantity formatting", 400)

        #Check if product exists and verify inventory
        item_rows = db.execute("SELECT * FROM items WHERE id = ?", item_id)
        if len(item_rows) != 1:
            return apology("item choice element not found in active data catalogs", 404)

        if item_rows[0]["qty"] < quantity:
            return apology("requested stock count exceeds active item warehouse inventory limits", 400)

        #Check if this user already has the same item in their cart table
        cart_rows = db.execute(
            "SELECT * FROM cart WHERE u_id = ? AND i_id = ?", user_id, item_id
        )

        if len(cart_rows) > 0:
            new_qty = cart_rows[0]["qty"] + quantity

            if new_qty > item_rows[0]["qty"]:
                return apology("combined selection count exceeds available stock allocations", 400)

            db.execute(
                "UPDATE cart SET qty = ? WHERE u_id = ? AND i_id = ?",new_qty, user_id, item_id)
        else:
            db.execute(
                "INSERT INTO cart (u_id, i_id, qty) VALUES (?, ?, ?)",user_id, item_id, quantity)

        flash("Item successfully added to your cart!")
        return redirect("/index")

    #handles GET method
    else:
        # Pull products joined through database ID relations to show items inside cart
        cart_items = db.execute("SELECT items.id, items.name, items.image, items.price, cart.qty FROM cart JOIN items ON cart.i_id = items.id WHERE cart.u_id = ?", user_id)

        if not cart_items:
            flash("No items in cart")

        # Calculate checkout numbers dynamically
        grand_total = sum(item["price"] * item["qty"] for item in cart_items)

        return render_template("cart.html", cart_items=cart_items, total=grand_total)



@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    if request.method == "GET":
        return redirect("/cart")
    else:
        return apology("Payments aren't supported yet", 400)
# payment gateway can be added here



# this code is inspired by cs50 finance distribution code but with a few modifications
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE name = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1:
            return redirect("/sign_up")

        input_pwd = request.form.get("password")

        if not rows[0]["pwd"] == input_pwd:
            return apology("invalid password or User Id", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        if rows[0]["name"].lower() == "admin":
            session["is_admin"] = True
        else:
            session["is_admin"] = False

        # Redirect user to home page
        return redirect("/index")

    else:
        return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/index")


@app.route("/sign_up", methods=["POST","GET"])
def sign_up():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        uname = request.form.get("uname")
        pwd = request.form.get("pwd")
        email = request.form.get("email")

        if not uname:
            return apology("Must enter name", 400)

        if not pwd:
            return apology("Must enter password", 400)

        if not pwd == (request.form.get("confirmpwd")):
            return apology("passwords didn't match", 400)

        if not email:
            return apology("invalid email", 400)


        rows = db.execute("select * from users where name=? or email=?", uname, email)
        if len(rows) >= 1:
            return apology(" username or email already in use", 400)

        db.execute("insert into users(name, pwd, email) values(?, ?, ?)", uname, pwd, email)
        flash("Sign up successful")

        return redirect("/index")


# the following admin route code is not completey mine , I have used chatgpt to refine it
# Prompt " Help me refine this code where I want only image file formats to be uploaded to the databse and reject the rest"
@app.route("/admin", methods=["GET", "POST"])
@admin_required
def admin_panel():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        qty = request.form.get("qty")
        description = request.form.get("description")
        keywords = request.form.get("keywords")

        if not name or not price or not qty:
            return apology("must provide name, price, and stock quantity", 400)

        if 'item_image' not in request.files:
            return apology("no image file uploaded", 400)

        if not description:
            return apology("please add description", 400)

        file = request.files['item_image']

        if file.filename == '':
            return apology("no selected image file", 400)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            db_image_path = f"items_img/{filename}"

            db.execute("insert into items (name, image, price, qty, keywords, description) VALUES (?, ?, ?, ?, ?, ?)",name, db_image_path, float(price), int(qty), keywords, description)

            flash("Item added to catalog successfully!")
            return redirect("/admin")
        else:
            return apology("invalid file type", 400)
    else:
        items = db.execute("SELECT * FROM items")
        return render_template("admin.html", items=items)

@app.route("/delete_item", methods=["POST"])
@admin_required
def delete():
    item_id = request.form.get("item_id")
    if not item_id:
        return apology("Can't remove the item", 400)
    else:
        db.execute("delete from cart where i_id=?", item_id)
        db.execute("delete from items where id=?", item_id)
        flash("Item deleted successfully")
        return redirect("/admin")

@app.route("/delete_cart", methods=["POST"])
@login_required
def cartdelete():

    item_id = request.form.get("item")
    if not item_id:
        return redirect("/cart")

    else:
        db.execute("delete from cart where u_id=? and i_id=?", session["user_id"], item_id)
        return redirect("/cart")
