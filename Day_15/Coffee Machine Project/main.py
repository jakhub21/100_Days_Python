MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources(resource, caffe):
    if resource['water'] >= caffe['ingredients']['water'] and resource['coffee'] >= caffe['ingredients']['coffee'] and resource['milk'] >= caffe['ingredients']['milk']:
        print(f"This is your cafe")
        resource['water'] -= caffe['ingredients']['water']
        resource['milk'] -= caffe['ingredients']['milk']
        resource['coffee'] -= caffe['ingredients']['coffee']
        resource['money'] += caffe['cost']
        return resource
    else:
        if resource['water'] < caffe['ingredients']['water']:
            print("There is to not enough water in the machine")
        elif resource['milk'] < caffe['ingredients']['milk']:
            print("There is to not enough milk in the machine")
        elif resource['coffe'] < caffe['ingredients']['coffee']:
            print("There is to not enough coffee in the machine")
        return resource


flag = True
while flag:
    data = input("What you want: Espresso/Latte/Cappuccino or report\n").lower()
    if data == "report":
        for i, j in resources.items():
            print(f"{i} : {j}")
    elif data == "espresso":
        caffe = MENU['espresso']
        resources = check_resources(resources, caffe)
    elif data == "latte":
        caffe = MENU['latte']
        resources = check_resources(resources, caffe)
    elif data == "cappuccino":
        caffe = MENU['cappuccino']
        resources = check_resources(resources, caffe)

