from flask import Flask, render_template, request, jsonify
import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('Agg') # Use non-interactive backend
import matplotlib.pyplot as plt
import io
import base64
import markdown
import os
import markdown
import os
import sys
from scipy.optimize import linprog

# Add parent directory to path to import projects
# The path is Math-with-Python-for-CS/projects/advanced
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(project_root, 'Math-with-Python-for-CS', 'projects', 'advanced'))

import rsa_encryption

app = Flask(__name__)

# Safe namespace for the Universal Solver
safe_dict = {
    'x': sp.symbols('x'),
    'y': sp.symbols('y'),
    'z': sp.symbols('z'),
    'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'exp': sp.exp, 
    'log': sp.log, 'sqrt': sp.sqrt, 'pi': sp.pi, 'oo': sp.oo,
    'integrate': sp.integrate,
    'diff': sp.diff,
    'solve': sp.solve,
    'limit': sp.limit,
    'Eq': sp.Eq,
    'Matrix': sp.Matrix
}

@app.route('/solver', methods=['GET', 'POST'])
def universal_solver():
    result = None
    if request.method == 'POST':
        command = request.form.get('command')
        try:
            # Dangerous in prod, acceptable for local demo
            # Eval the command in the safe sympy namespace
            output = eval(command, {"__builtins__": None}, safe_dict)
            result = sp.latex(output)
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('tool_solver.html', result=result)

@app.route('/optimize', methods=['GET', 'POST'])
def optimize_tool():
    result = None
    if request.method == 'POST':
        try:
            # Parse inputs (expecting comma/newline separated values)
            c_str = request.form.get('c') # Objective coefficients
            A_str = request.form.get('A') # Inequality Matrix
            b_str = request.form.get('b') # Inequality Vector
            
            # Convert strings to arrays
            c = [float(x) for x in c_str.split(',')]
            b = [float(x) for x in b_str.split(',')]
            
            # Parse Matrix A (rows separated by newlines, cols by commas)
            A = []
            for row in A_str.strip().split('\n'):
                A.append([float(x) for x in row.split(',')])
            
            # Default bounds (x >= 0)
            res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')
            
            if res.success:
                result = f"Optimal Value: {res.fun:.4f}\nAt x = {res.x}"
            else:
                result = f"Optimization Failed: {res.message}"
        except Exception as e:
            result = f"Error parsing input: {str(e)}"
            
    return render_template('tool_optimize.html', result=result)
# ... (existing routes) ...

@app.route('/rsa', methods=['GET', 'POST'])
def rsa_tool():
    result = None
    public_key = None
    private_key = None
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'generate':
            p = int(request.form.get('p'))
            q = int(request.form.get('q'))
            try:
                public_key, private_key = rsa_encryption.generate_keypair(p, q)
                result = "Keys Generated Successfully!"
            except ValueError as e:
                result = f"Error: {str(e)}"
                
        elif action == 'encrypt':
            message = request.form.get('message')
            e_key = int(request.form.get('e_key'))
            n_key = int(request.form.get('n_key'))
            try:
                cipher = rsa_encryption.encrypt((e_key, n_key), message)
                result = f"Encrypted Message: {cipher}"
            except Exception as e:
                result = f"Error: {str(e)}"
                
        elif action == 'decrypt':
            # Handling list input from string is tricky in simple form, 
            # let's assume input is comma separated numbers
            cipher_str = request.form.get('ciphertext')
            d_key = int(request.form.get('d_key'))
            n_key = int(request.form.get('n_key'))
            try:
                cipher = [int(x.strip()) for x in cipher_str.split(',')]
                plain = rsa_encryption.decrypt((d_key, n_key), cipher)
                result = f"Decrypted Message: {plain}"
            except Exception as e:
                 result = f"Error: {str(e)}"

    return render_template('tool_rsa.html', result=result, public_key=public_key, private_key=private_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/limit', methods=['GET', 'POST'])
def limit_tool():
    result = None
    if request.method == 'POST':
        expr_str = request.form.get('expression')
        point = request.form.get('point')
        try:
            x = sp.symbols('x')
            expr = sp.sympify(expr_str)
            if point == 'infinity':
                lim = sp.limit(expr, x, sp.oo)
            else:
                lim = sp.limit(expr, x, float(point))
            result = f"Limit of {expr_str} as x -> {point} is: {lim}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('tool_limit.html', result=result)

@app.route('/derivative', methods=['GET', 'POST'])
def derivative_tool():
    result = None
    if request.method == 'POST':
        expr_str = request.form.get('expression')
        try:
            x = sp.symbols('x')
            expr = sp.sympify(expr_str)
            diff = sp.diff(expr, x)
            result = f"Derivative of {expr_str} is: {diff}"
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('tool_derivative.html', result=result)

@app.route('/plot_distribution')
def plot_distribution():
    # Generate plot for Normal Distribution
    img = io.BytesIO()
    x = np.linspace(-4, 4, 100)
    y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
    
    plt.figure(figsize=(6, 4))
    plt.plot(x, y)
    plt.title("Standard Normal Distribution")
    plt.xlabel("x")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('tool_distribution.html', plot_url=plot_url)

@app.route('/content/<path:filename>')
def render_content(filename):
    """
    Renders a markdown file from the repository as HTML.
    """
    # Security check: ensure path is within allowed directories
    allowed_dirs = ['01-Calculus', '02-Probability-Statistics', '03-Discrete-Math', '04-Linear-Algebra', '05-Permutation-Combination', '06-Graphs-Advanced-Topics', 'CS-Interview-Math']
    
    # Construct absolute path to the file
    # Assuming app.py is in web_app/, we go up one level
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    # Check if the requested file starts with an allowed directory
    safe = False
    for d in allowed_dirs:
        if filename.startswith(d):
            safe = True
            break
            
    if not safe:
        return "Access Denied", 403
        
    filepath = os.path.join(base_dir, filename)
    
    if not os.path.exists(filepath):
        return "File Not Found", 404
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    # Convert Markdown to HTML
    html_content = markdown.markdown(content, extensions=['fenced_code', 'tables'])
    
    return render_template('content.html', content=html_content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
