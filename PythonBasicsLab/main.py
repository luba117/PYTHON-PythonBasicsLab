import logging
import os
from datetime import datetime

from calculator import Calculator
from control_flow import if_demo, for_demo, while_demo
from lists_generator_demo import list_vs_generator_demo


log_directory = "logs"
if not os.path.exists(log_directory):  
    os.makedirs(log_directory)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(log_directory, "app.log")),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def task1_environment_setup():
    """Task 1: Python installation, IDEs, Jupyter setup"""
    print_header("TASK 1: ENVIRONMENT SETUP")
    
    print(f"\n Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Current Directory: {os.getcwd()}")
    print(f" Log Directory: {log_directory}/")
    print(f" Logging configured: app.log")
    
    # Create test directories if needed
    os.makedirs("tests", exist_ok=True)
    print(" Environment setup complete")

def task2_calculator_demo():
    """Task 2,4,5: Calculator with variables, operators, error handling"""
    print_header("TASK 2,4,5: CALCULATOR DEMO")
    
    calc = Calculator()
    
    # Basic operations
    print("\nBasic Calculator Operations:")
    print(f"{calc.add(10, 5)}")
    print(f"{calc.subtract(10, 5)}")
    print(f"{calc.multiply(10, 5)}")
    print(f"{calc.divide(10, 5)}")
    
    # Error handling demo
    print("\n⚠️ Error Handling Demo:")
    try:
        calc.divide(10, 0)
    except Calculator.CalculatorError as e:
        print(f"Caught error: {e}")
    
    try:
        calc.add(10, "5")
    except Calculator.CalculatorError as e:
        print(f"   Caught error: {e}")
    
    # Variable types demo
    print("\n Variable Types:")
    integer_var = 42
    float_var = 3.14
    string_var = "Python Lab"
    boolean_var = True
    list_var = [1, 2, 3, 4, 5]
    
    print(f"   Integer: {integer_var} ({type(integer_var).__name__})")
    print(f"   Float: {float_var} ({type(float_var).__name__})")
    print(f"   String: {string_var} ({type(string_var).__name__})")
    print(f"   Boolean: {boolean_var} ({type(boolean_var).__name__})")
    print(f"   List: {list_var} ({type(list_var).__name__})")
    
    logger.info("Calculator demo completed")

def task3_control_flow_demo():  
    print_header("TASK 3: CONTROL FLOW DEMO")
    
    # If statement demo
    print("\n If Statement Demo:")
    test_values = [-5, 0, 7]
    for val in test_values:
        result = if_demo(val)
        print(f"   if_demo({val}) → {result}")
    
    # For loop demo
    print("\n🔄 For Loop Demo:")
    for_results = for_demo()
    for item in for_results:
        print(f"   {item}")
    
    # While loop demo
    print("\n⏱️ While Loop Demo:")
    while_results = while_demo()
    for item in while_results:
        print(f"   {item}")
    
    logger.info("Control flow demo completed")

def task6_cloud_ready():
    """Task 6: Cloud deployment ready"""
    print_header("TASK 6: CLOUD READY")
    
    cloud_features = [
        "✅ Environment variables configured",
        "✅ Logging configured for cloud",
        "✅ Error handling implemented",
        "✅ Stateless design",
        "✅ Ready for AWS Lambda / Azure Functions"
    ]
    
    for feature in cloud_features:
        print(f"   {feature}")

def task8_github_ready():
    """Task 8: GitHub ready"""
    print_header("TASK 8: GITHUB READY")
    
    print("\n📁 Repository Structure:")
    structure = """
    python-basics-lab/
    ├── 📄 main.py (or Program.py)
    ├── 📄 calculator.py
    ├── 📄 control_flow.py
    ├── 📁 logs/
    │   └── 📄 app.log
    ├── 📁 tests/
    │   └── 📄 test_calculator.py
    ├── 📄 requirements.txt
    ├── 📄 README.md
    └── 📄 .gitignore
    """
    print(structure)
    
    print("\n📌 Git Commands:")
    commands = [
        "git init",
        "git add .",
        'git commit -m "Initial commit: Python Fundamentals Lab"',
        "git branch -M main",
        "git remote add origin https://github.com/yourusername/python-basics-lab.git",
        "git push -u origin main"
    ]
    
    for i, cmd in enumerate(commands, 1):
        print(f"   {i}. {cmd}")

def verify_logging():
    """Verify logging is working"""
    print_header("LOGGING VERIFICATION")
    
    log_file = os.path.join(log_directory, "app.log")
    if os.path.exists(log_file):
        print(f"✅ Log file created: {log_file}")
        
        # Show last few log entries
        with open(log_file, 'r') as f:
            lines = f.readlines()
            if lines:
                print(f"\n📝 Last 3 log entries:")
                for line in lines[-3:]:
                    print(f"   {line.strip()}")
    else:
        print(f"❌ Log file not found: {log_file}")

def main():
    """Main function to run all tasks"""
    
    print("\n" + "*" * 30)
    print("   PYTHON FUNDAMENTALS LAB")
    print("*" * 30)
    
    # Run all tasks
    task1_environment_setup()
    task2_calculator_demo()
    task3_control_flow_demo()   
    task8_github_ready()
    list_vs_generator_demo()
    
    # Verify logging
    verify_logging()
    
    # Summary
    print_header("LAB COMPLETED SUCCESSFULLY! 🎉")
    print("\n✅ All tasks completed:")
    print("   • Task 1: Environment Setup")
    print("   • Task 2: Variables, Data Types, Operators")
    print("   • Task 3: Control Flow (if/for/while)")
    print("   • Task 4: Unit Tests (in tests/ folder)")
    print("   • Task 5: Logging & Error Handling") 
    print("   • Task 6: GitHub Ready")
    
    print(f"\n📊 Check '{log_directory}/app.log' for detailed logs")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Program interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        logger.error(f"Unexpected error in main: {e}", exc_info=True)
    finally:
        print("\n👋 Created by Luba Moura Goodbye!")