# E-Commerce Web Application

#### Video Demo: (https://youtu.be/OC65Y3Frj3s)

#### **Github Username:** trynafindmatrix
#### **Date:** 16 Aug 2026

### Key Features
* **User Authentication:** Secure registration and login system. Sessions are used to keep logged in, and passwords are stored in the database.
* **Landing Page:** A landing page for representing information about the services/products and ***company***.
* **Product Browsing:** Interactive interface to browse prodcuts and view detailed information.
* **Shopping Cart:** Add, remove, and manage items ready for purchase.
* **Admin Pannel:** Admin can add and manage items/products in the catalog.

### Tech Stack & Dependencies
The application was built using a mix of modern frontend and backend technologies:
* **Backend:** Python and Flask to handle application logic and routing.
* **Database:** SQLite to manage users, products, cart information and saved items/prodcuts. The database effectively connects users with the products they save.
* **Front-end:** HTML, CSS, JavaScript, and Bootstrap for a clean, responsive interface.
* **Libraries:** Flask, CS50, Bootstrap, werkzeug.utils, Flask-Session, pytz, requests.


## Project Overview
 My E-Commerce Web Application is a robust, secure, and fully responsive e-commerce web application engineered to bridge corporate identity with an active digital storefront. Built with a clear separation of concerns, the platform serves a dual purpose: acting as an informational company portfolio while simultaneously delivering a functional, database-driven shopping network. The system architecture balances open-source public browsing with strict multi-tiered authentication barriers to protect session data and administrative control mechanisms.

### Inspiration and Core Problem Solved
Traditional small-business websites are often fragmented, forcing business owners to manage an informational site on one platform and an expensive third-party store on another. This project solves that fragmentation by unifying a corporate landing page, service catalogs, an active customer shopping matrix, and an executive administrative back-end into a single, cohesive ecosystem. Developing this application represented a major leap in complexity over standard CS50 problem sets (like Finance), requiring complex relational database schema tracking, state preservation for individual user carts, and rigid permission controls to separate standard customers from administrative managers. And also I built this project to apply the concepts and languages which I learned throughout CS50x-particularly **Python, SQL, Flask, databases, authentication, HTML, CSS and JavaScript**.

### User Experience & Public Navigation Flow
When an anonymous guest arrives at the platform, they land on a comprehensive corporate homepage detailing the company’s history, core philosophy, and overarching mission. A persistent navigation bar allows fluid traversal to a dedicated Services and Products page, which lists the company's professional offerings. To engage in digital commerce, the navigation bar features a direct portal to the Shop.The application implements a strict permission structure to guarantee data safety and clean session parsing:
#### Anonymous Guests:
 Unauthenticated users possess full read-only rights. They can seamlessly browse the entire digital catalog, inspect product details, and evaluate pricing metrics. However, any attempt to execute write operations—such as clicking the "Add to Cart" mechanism—is immediately intercepted. The application smoothly redirects the user to a secure authentication gateway where they can quickly Log In or, if a record is not found, Sign Up for a new account.
 #### Authenticated Users:
 Once securely logged in via session tokens, users unlock full transactional capabilities. They can populate their personal shopping carts dynamically, with the database ensuring their cart state remains intact across browser sessions.

 ### Cart Logic, Grand Total, and Checkout Solution
 The shopping cart interface acts as a personal financial ledger for the logged-in user. Every time an item is added, a backend database entry links the unique user ID with the specific product ID. Within the cart interface, users can audit their choices in real-time, executing updates or removing items completely. The application dynamically processes these deletions, recalculating the financial matrices and updating the Grand Total instantly using floating-point optimization to prevent compounding currency rounding errors.A major architectural consideration during development was handling the final Checkout phase. Due to security considerations and the advanced complexity curves surrounding third-party financial gateways (such as Stripe or PayPal APIs), a live live payment processing pipeline was intentionally left out of this build cycle. Instead of integrating a vulnerable or half-implemented financial endpoint, a controlled, user-friendly fallback page was engineered. Clicking the checkout button safely routes the user to a dedicated informational screen explicitly stating "Payments aren't supported yet." This demonstrates robust error boundaries and a commitment to transparent user interface design, prioritizing data safety.
 ### Administrative Control Panel

 To provide complete business utility, the application implements a privileged administrative layer. When a user logs in with verified administrative credentials, the application recognizes their high-level authorization tier and exposes a restricted Admin Panel link in the navigation system.
 This secure dashboard serves as the command center for the digital storefront, giving the administrator direct Create, Read, Update, and Delete (CRUD) access to the inventory database:
 Inventory Expansion: The admin can dynamically inject new items into the marketplace by completing a structured form that pushes new data rows directly into the shop's database table.
 Inventory Retraction: If a product becomes unavailable or obsolete, the admin can completely remove the item from the catalog with a single action, instantly cascading the deletion across the public shop views.

#### Description:
This project is an **e-commerce web application** developed as my final project for **CS50**. The application allows users to create account, log in, log out, browse products, view prodcut details, add products to a shopping cart and manage their saved products. It also include a admin pannel where admin can add products and related details, and remove produts from the catalog.


---

## File Structure & Breakdown

├── app.py
├── helpers.py
├── requirements.txt
├── README.md
├── data.db
├── static/
│   ├── styles.css
│   └── items_img/
│        └── (stores the image files)
│
├── flask_session/
│   └──(stores sessions data)
│
└── templates/
    ├── layout.html
    ├── index.html
    ├── login.html
    ├── admin.html
    ├── apology.html
    ├── cart.html
    ├── homepage.html
    └── signup.html

### Detailed File Descriptions:
* **`app.py`:** This is the main driver of the application. It contains all the routing logic, handles session management, connects to the database, and processes incoming POST/GET requests.
* **`helpers.py`:** Contains utility functions designed to keep the codebase DRY (Don't Repeat Yourself). This includes login decorators and error handling configurations.
* **`requirements.txt`:** Flask, CS50, Flask-Session, pytz, requests.
* **`data.db`:** The relational database file. It contains schemas for users, cart , and items. Ensuring strict data persistence across sessions.
* **`static/styles.css`:** Holds the custom UI styling, layout positioning, and design aesthetics for the application.
* **`templates/layout.html`:** The skeletal base structural blueprint for all pages (except homepage.html), utilizing block tags to allow dynamic template inheritance.
* **`templates/homepage.html`:** The landing page. It also connects the user to the templates/index.html.
* **`templates/index.html`:** The primary user dashboard. It dynamically populates personalized data matrices depending on the active user session.

## Design Choices & Challenges
I used a dark theme along with bright blue color containers for my project to make it look diffirent and unique. I also used cs50 finance apology function because I liked that grumpy cat error message and its dynamicity. The hardest bug I faced was to limit the "admin" to upload only image files like(.jpeg, .png, .jpg and .gif), for this I used an array with the allowed file format and to compare the uploaded file format and to refine that I used Chatgpt and promt (" Help me refine this code where I want only image file formats to be uploaded to the databse and reject the rest"). I also used Chatgpt for some other debugging when I couldn't pinpoint the cause of the error.

## Setup & Installation Instruction

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd project
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize the database:**
   (Explain any commands needed to set up or seed tables)

4. **Run the local development server:**
   ```bash
   flask run
   ```
5. **Admin must sign up and login with the username ***admin*** and password of your choice.

## Future Features & Project Roadmap
While the current iteration of the application provides a robust foundation for corporate presentation, customer cart orchestration, and administrative inventory control, there are several scaling vectors and advanced features earmarked for future development cycles:

### dark/Light Theme Toggle:
to enable users to chnage the theme as per their prefernce. I tried to implement it but I came accros some unexpectd bugs and difficulties which made me put this featutre in the future plan.

### Secure Payment Gateway Integration:
Transition from the current simulation placeholder ("Payments aren't supported yet") to a production-ready financial pipeline.
Integrate third-party sandboxed REST APIs such as Stripe or PayPal to support compliant, tokenized credit card transactions.
Implement webhooks to securely listen for successful payment events before committing transactional logs to the database.

### Advanced Admin Analytics & Reporting:
Expand the Admin Panel into a comprehensive business intelligence dashboard.
Integrate data visualization libraries (like Chart.js or D3.js) to render interactive graphs tracking monthly revenue curves, top-selling items, and conversion metrics.
Add automated inventory alerts that notify the administrator via email when stock thresholds drop below a specific limit.

### Persistent User Profiles & Order History:
Engineer a post-checkout relational table schema linking user IDs to finalized invoices.
Develop a customer dashboard allowing users to view chronological order receipts, tracking statuses, and download PDF invoices.
Allow users to securely save multiple shipping configurations and default payment methods to expedite the checkout funnel.

### Marketing and account recovery support
The database already consists keywords for each item/product which can help to implement future search feature and also it can help in SEO. The database also stores email of each user which can be used as targeted marketing and for recovering or managing user's accounts.
