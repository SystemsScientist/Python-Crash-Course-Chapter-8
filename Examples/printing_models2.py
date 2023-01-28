# printing_models2.py, Chapter 8, Python Crash Course
# program prints a list of completed designs

def print_models(unprinted_designs, completed_models):
    """
    simulate printing each design until none are left
    move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # simulate creating a 3D print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)



