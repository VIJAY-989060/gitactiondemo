from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return """
    <h1>Welcome to My Flask App on AWS EC2!</h1>
    <p>This app is deployed automatically using GitHub Actions 🚀</p>
    <p><a href='/calc'>Go to Calculator</a></p>
    """

# Simple Calculator Page
@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method == "POST":
        try:
            a = int(request.form["a"])
            b = int(request.form["b"])
            result = a + b
            return render_template_string("""
                <h2>Result: {{a}} + {{b}} = {{result}}</h2>
                <a href='/calc'>Try Again</a>
            """, a=a, b=b, result=result)
        except:
            return "Invalid input. Please enter numbers only."
    
    return """
    <form method="post">
        <input type="text" name="a" placeholder="Enter number A" required>
        <input type="text" name="b" placeholder="Enter number B" required>
        <button type="submit">Add</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
