from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
import os

app = Flask(__name__)

# Ensure the static folder exists for storing images
os.makedirs('static/images', exist_ok=True)

# Database setup
DB_FILE = 'orders.db'

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            region TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL
        )
        ''')
        conn.commit()

init_db()

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HICHEM VAISSELLE DAMOUS</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                text-align: center;
                background-color: #f9f9f9;
            }
            .header {
                background-color: orange;
                padding: 20px;
                color: white;
                font-size: 70px;
                font-weight: bold;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }
            .header img {
                width: 130px;
                height: auto;
                margin-left: 40px;
                vertical-align: middle;
            }
            /* Updated and more visually appealing promo box */
            .promo-box {
                position: relative;
                top: 0;
                background: linear-gradient(135deg, rgba(255, 140, 0, 0.8), rgba(255, 95, 0, 0.8)); /* Gradient background */
                color: white;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.2);
                width: 80%;
                margin: 20px auto;
                text-align: center;
                font-size: 26px;
                font-weight: bold;
            }
            .promo-text {
                font-size: 50px;
                color: #ff5a00;
                font-weight: bold;
            }
            .promo-subtext {
                font-size: 18px;
                color: white;
                margin-top: 10px;
            }
            .product {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin: 20px;
            }
            .product img {
                max-width: 100%;
                max-height: 500px;
                object-fit: contain;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 10px;
            }
            .thumbnail-images {
                margin-top: 20px;
                display: flex;
                justify-content: center;
                gap: 10px;
            }
            .thumbnail {
                width: 80px;
                height: auto;
                cursor: pointer;
                border: 2px solid #ddd;
                border-radius: 8px;
            }
            .thumbnail:hover {
                border-color: orange;
            }
            .form {
                margin: 20px;
                text-align: right;
                display: inline-block;
                width: 80%;
            }
            .form input, .form select {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            .order-button {
                background-color: red;
                color: white;
                padding: 15px;
                font-size: 30px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
            }
            .footer {
                margin-top: 20px;
            }
            .footer a {
                text-decoration: none;
                color: white;
                background-color: #3b5998;
                padding: 10px;
                border-radius: 5px;
            }
            /* Text description box styles */
            .product-description {
                background-color:rgb(129, 124, 124); /* Tomato color */
                color: white;
                font-family: 'Courier New', Courier, monospace;
                font-weight: bold;
                padding: 20px;
                border-radius: 10px;
                width: 90%;
                margin: 20px auto;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .product-description h2 {
                font-size: 24px;
                text-decoration: underline;
                color: white;
                margin-bottom: 10px;
            }
            .product-description p {
                font-size: 18px;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <img src="/static/images/logo.png" alt="Logo">
            HICHEM VAISSELLE DAMOUS
            <img src="/static/images/logo.png" alt="Logo 2">
        </div>

        <!-- Updated and visually enhanced promo box -->
        <div class="promo-box">
            <div class="promo-text">أطلب الآن ! و اغتنم الفرصة التي لاتتعوض !</div>
            <div class="promo-subtext">• PROMO #2025 •</div>
        </div>

        <div class="product">
            <img id="main-image" src="/static/images/product.jpg" alt="Product Image">
            <div class="thumbnail-images">
                <img src="/static/images/logo1.jpg" alt="Thumbnail 1" class="thumbnail" onclick="changeImage('/static/images/logo1.jpg')">
                <img src="/static/images/logo2.jpg" alt="Thumbnail 2" class="thumbnail" onclick="changeImage('/static/images/logo2.jpg')">
                <img src="/static/images/logo3.jpg" alt="Thumbnail 2" class="thumbnail" onclick="changeImage('/static/images/logo3.jpg')">
                <img src="/static/images/logo4.jpg" alt="Thumbnail 2" class="thumbnail" onclick="changeImage('/static/images/logo4.jpg')">
                <img src="/static/images/logo5.jpg" alt="Thumbnail 2" class="thumbnail" onclick="changeImage('/static/images/logo5.jpg')">
                <img src="/static/images/logo6.jpg" alt="Thumbnail 2" class="thumbnail" onclick="changeImage('/static/images/logo6.jpg')">
                <img src="/static/images/logo7.jpg" alt="Thumbnail 2" class="thumbnail" onclick="changeImage('/static/images/logo7.jpg')">
                <img src="/static/images/logo8.jpg" alt="Thumbnail 2" class="thumbnail" onclick="changeImage('/static/images/logo8.jpg')">
            </div>
        </div>

        <!-- Product description with style -->
        <div class="product-description">
            <h2>طابونة عصرية</h2>
            <p>سعر: 11800دج (مليون ومية وثمانين الف)</p>
            <p>والتوصيل مجاني لباب الدار يعني حتى تشوفها قدامك باش تخلص😍😍😍</p>
            <p>طابونة 80سم المتعددة الإستعمالات بطول 80سم 😍 + طاجين من الحديد الخشن (مايحرقش) لتسهيل أي نوع من الطهي😋😋 (كسرة، محاجب، لحم، فريت أوملات، ووووو) + 💥 شبكة من الحديد متعددة الإستعمالات 🎁</p>
            <p>التوصيل راه مجاني لباب الدار. عرض مؤقت فقط 📢</p>
        </div>

        <form class="form" action="/submit" method="POST">
            <input type="text" name="full_name" placeholder="الاسم الكامل" required>
            <select name="region" required>
                <option value="">اختر الولاية</option>
                <option value="تيبازة">تيبازة</option>
                <option value="الجزائر">الجزائر</option>
                <option value="تيزي وزو">تيزي وزو</option>
            </select>
            <input type="text" name="address" placeholder="أدخل العنوان" required>
            <input type="text" name="phone" placeholder="أدخل رقم الهاتف" required>
            <button type="submit" class="order-button">أطلب الآن</button>
        </form>

        <div class="footer">
            <a href="https://www.facebook.com/hichem.vaisselle42/" target="_blank">صفحتنا على الفيسبوك</a>
        </div>

        <script>
            function changeImage(src) {
                document.getElementById("main-image").src = src;
            }
        </script>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    full_name = request.form['full_name']
    region = request.form['region']
    address = request.form['address']
    phone = request.form['phone']

    # Insert order into the database
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO orders (full_name, region, address, phone) 
        VALUES (?, ?, ?, ?)
        ''', (full_name, region, address, phone))
        conn.commit()
        order_id = cursor.lastrowid

    # Redirect to confirmation page
    return redirect(f'/confirmation/{order_id}')


@app.route('/confirmation/<int:order_id>')
def confirmation(order_id):
    return f'''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>تأكيد الطلب</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f9f9f9;
                margin: 0;
                padding: 20px;
            }}
            h1 {{
                color: green;
                font-size: 50px;
            }}
            p {{
                font-size: 20px;
                margin: 10px 0;
            }}
            .confirmation-box {{
                margin-top: 30px;
                padding: 20px;
                background-color: #fff;
                border: 1px solid #ddd;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .return-button {{
                margin-top: 20px;
                display: inline-block;
                padding: 10px 20px;
                font-size: 20px;
                background-color: orange;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }}
            .info-box {{
                margin-top: 40px;
                padding: 20px;
                background-color: #eee;
                border-radius: 10px;
            }}
            .info-box h3 {{
                font-size: 24px;
                color: #333;
                text-decoration: underline;
            }}
            .info-box p {{
                font-size: 18px;
                color: #555;
            }}
            .verified-img {{
                width: 120px;
                margin-bottom: 20px;
                animation: swing 1s infinite; /* الحركة */
            }}
            @keyframes swing {{
                0% {{ transform: rotate(0deg); }}
                25% {{ transform: rotate(10deg); }}
                50% {{ transform: rotate(0deg); }}
                75% {{ transform: rotate(-10deg); }}
                100% {{ transform: rotate(0deg); }}
            }}
        </style>
    </head>
    <body>
        <div class="confirmation-box">
            <img src="/static/images/verified.png" alt="تم التحقق" class="verified-img">
            <h1>تم التأكيد ✅</h1>
            <p>شكرًا على طلبك</p>
            <p>رقم الطلبية: {order_id}</p>
            <p>رقم الهاتف لتأكيد الطلب: 0656510607</p>
            <a href="/" class="return-button">العودة إلى الموقع</a>
        </div>
        <div class="info-box">
            <h3>معلومات عنا</h3>
            <p>العنوان: الداموس وسط المدينة - تيبازة</p>
            <p>الهاتف المحل: 0553672453</p>
            <p>البريد الألكتروني : nadjib-18@live.fr</p>
        </div>
    </body>
    </html>
    '''



if __name__ == '__main__':
    app.run(debug=True)
