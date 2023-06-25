import json
import openai
from collections import defaultdict
from typing import Dict, List, Any, Union

products_file = "../../data/product_info.json"
categories_file = "../../data/categories.json"

delimiter = "####"
step_2_system_message_content = f"""
You will be provided with customer service a conversation. \
The most recent user query will be delimited with \
{delimiter} characters.
Output a python list of objects, where each object has \
the following format:
    'category': <one of Computers and Laptops, \
    Smartphones and Accessories, \
    Televisions and Home Theater Systems, \
    Gaming Consoles and Accessories, 
    Audio Equipment, Cameras and Camcorders>,
OR
    'products': <a list of products that must \
    be found in the allowed products below>

Where the categories and products must be found in \
the customer service query.
If a product is mentioned, it must be associated with \
the correct category in the allowed products list below.
If no products or categories are found, output an \
empty list.
Only list products and categories that have not already \
been mentioned and discussed in the earlier parts of \
the conversation.

Allowed products: 

Computers and Laptops category:
TechPro Ultrabook
BlueWave Gaming Laptop
PowerLite Convertible
TechPro Desktop
BlueWave Chromebook

Smartphones and Accessories category:
SmartX ProPhone
MobiTech PowerCase
SmartX MiniPhone
MobiTech Wireless Charger
SmartX EarBuds

Televisions and Home Theater Systems category:
CineView 4K TV
SoundMax Home Theater
CineView 8K TV
SoundMax Soundbar
CineView OLED TV

Gaming Consoles and Accessories category:
GameSphere X
ProGamer Controller
GameSphere Y
ProGamer Racing Wheel
GameSphere VR Headset

Audio Equipment category:
AudioPhonic Noise-Canceling Headphones
WaveSound Bluetooth Speaker
AudioPhonic True Wireless Earbuds
WaveSound Soundbar
AudioPhonic Turntable

Cameras and Camcorders category:
FotoSnap DSLR Camera
ActionCam 4K
FotoSnap Mirrorless Camera
ZoomMaster Camcorder
FotoSnap Instant Camera

Only output the list of objects, with nothing else.
"""

step_2_system_message = {"role": "system", "content": step_2_system_message_content}


step_4_system_message_content = f"""
    You are a customer service assistant for a large electronic store. \
    Respond in a friendly and helpful tone, with VERY concise answers. \
    Make sure to ask the user relevant follow-up questions.
"""

step_4_system_message = {"role": "system", "content": step_4_system_message_content}

step_6_system_message_content = f"""
    You are an assistant that evaluates whether \
    customer service agent responses sufficiently \
    answer customer questions, and also validates that \
    all the facts the assistant cites from the product \
    information are correct.
    The conversation history, product information, user and customer \
    service agent messages will be delimited by \
    3 backticks, i.e. ```.
    Respond with a Y or N character, with no punctuation:
    Y - if the output sufficiently answers the question \
    AND the response correctly uses product information
    N - otherwise

    Output a single letter only.
"""

step_6_system_message = {"role": "system", "content": step_6_system_message_content}


def get_completion_from_messages(
    messages, model="gpt-3.5-turbo", temperature=0, max_tokens=500
) -> str:
    """
    Returns a mesage from LLM.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]


def create_categories() -> Dict[str, List[str]]:
    """
    Returns a dictionary where keys are categories and each value is a list of sub-categories in that category.
    """
    categories_dict = {
        "Billing": [
            "Unsubscribe or upgrade",
            "Add a payment method",
            "Explanation for charge",
            "Dispute a charge",
        ],
        "Technical Support": [
            "General troubleshooting" "Device compatibility",
            "Software updates",
        ],
        "Account Management": [
            "Password reset" "Update personal information",
            "Close account",
            "Account security",
        ],
        "General Inquiry": [
            "Product information" "Pricing",
            "Feedback",
            "Speak to a human",
        ],
    }

    with open(categories_file, "w") as file:
        json.dump(categories_dict, file)

    return categories_dict


def get_categories() -> Dict[str, List[str]]:
    """
    Returns a dictionary where keys are categories and each value is a list of sub-categories in that category.
    """
    with open(categories_file, "r") as file:
        categories = json.load(file)
    return categories


def get_product_list() -> List[str]:
    """
    Returns a list of product names.
    """
    products = get_products()
    product_list = []
    for product in products.keys():
        product_list.append(product)

    return product_list


def get_products_and_category() -> Dict[str, List[str]]:
    """
    Returns a dictionary where keys are categories and each value is a list of product names in that category.
    """
    products = get_products()
    products_by_category = defaultdict(list)
    for product_name, product_info in products.items():
        category = product_info.get("category")
        if category:
            products_by_category[category].append(product_info.get("name"))

    return dict(products_by_category)


def get_products() -> Dict[str, Dict[str, Any]]:
    """
    Returns a dictionary where keys are product names and each value is a dictionary of product information.
    """
    with open(products_file, "r") as file:
        products = json.load(file)
    return products


def find_category_and_product(user_input, products_and_category) -> str:
    delimiter = "####"
    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be delimited with {delimiter} characters.
    Output a python list of json objects, where each object has the following format:
        'category': <one of Computers and Laptops, Smartphones and Accessories, Televisions and Home Theater Systems, \
    Gaming Consoles and Accessories, Audio Equipment, Cameras and Camcorders>,
    OR
        'products': <a list of products that must be found in the allowed products below>

    Where the categories and products must be found in the customer service query.
    If a product is mentioned, it must be associated with the correct category in the allowed products list below.
    If no products or categories are found, output an empty list.

    The allowed products are provided in JSON format.
    The keys of each item represent the category.
    The values of each item is a list of products that are within that category.
    Allowed products: {products_and_category}
    
    """
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{delimiter}{user_input}{delimiter}"},
    ]
    return get_completion_from_messages(messages)


def find_category_and_product_only(user_input, products_and_category) -> str:
    """
    Returns a string that has a list of dictionary containing category and product names found in the user input.
    """
    delimiter = "####"
    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be delimited with {delimiter} characters.
    Output a python list of objects, where each object has the following format:
    'category': <one of Computers and Laptops, Smartphones and Accessories, Televisions and Home Theater Systems, \
    Gaming Consoles and Accessories, Audio Equipment, Cameras and Camcorders>,
    OR
    'products': <a list of products that must be found in the allowed products below>

    Where the categories and products must be found in the customer service query.
    If a product is mentioned, it must be associated with the correct category in the allowed products list below.
    If no products or categories are found, output an empty list.

    Allowed products: 
    Computers and Laptops category:
TechPro Ultrabook
BlueWave Gaming Laptop
PowerLite Convertible
TechPro Desktop
BlueWave Chromebook

Smartphones and Accessories category:
SmartX ProPhone
MobiTech PowerCase
SmartX MiniPhone
MobiTech Wireless Charger
SmartX EarBuds

Televisions and Home Theater Systems category:
CineView 4K TV
SoundMax Home Theater
CineView 8K TV
SoundMax Soundbar
CineView OLED TV

Gaming Consoles and Accessories category:
GameSphere X
ProGamer Controller
GameSphere Y
ProGamer Racing Wheel
GameSphere VR Headset

Audio Equipment category:
AudioPhonic Noise-Canceling Headphones
WaveSound Bluetooth Speaker
AudioPhonic True Wireless Earbuds
WaveSound Soundbar
AudioPhonic Turntable

Cameras and Camcorders category:
FotoSnap DSLR Camera
ActionCam 4K
FotoSnap Mirrorless Camera
ZoomMaster Camcorder
FotoSnap Instant Camera
    
    Only output the list of objects, nothing else.
    """
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{delimiter}{user_input}{delimiter}"},
    ]
    return get_completion_from_messages(messages)


def get_products_from_query(user_msg: str) -> str:
    """
    Returns a string from LLM that has a list of dictionary containing category and product names found in the user input.
    """
    products_and_category = get_products_and_category()
    delimiter = "####"
    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be delimited with {delimiter} characters.
    Output a python list of json objects, where each object has the following format:
        'category': <one of Computers and Laptops, Smartphones and Accessories, Televisions and Home Theater Systems, \
    Gaming Consoles and Accessories, Audio Equipment, Cameras and Camcorders>,
    OR
        'products': <a list of products that must be found in the allowed products below>

    Where the categories and products must be found in the customer service query.
    If a product is mentioned, it must be associated with the correct category in the allowed products list below.
    If no products or categories are found, output an empty list.

    The allowed products are provided in JSON format.
    The keys of each item represent the category.
    The values of each item is a list of products that are within that category.
    Allowed products: {products_and_category}

    """

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{delimiter}{user_msg}{delimiter}"},
    ]
    category_and_product_response = get_completion_from_messages(messages)

    return category_and_product_response


# product look up (either by category or by product within category)
def get_product_by_name(name: str) -> Union[Dict[str, Any], None]:
    """
    Returns a dictionary of product information for the given product name.
    """
    products = get_products()
    return products.get(name, None)


def get_products_by_category(category: str) -> List[Dict[str, Any]]:
    """
    Returns a list of dictionaries of product information for the given category.
    """
    products = get_products()
    return [product for product in products.values() if product["category"] == category]


def get_mentioned_product_info(data_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Returns a list of dictionaries of product information for the given list of data.
    """
    product_info_l = []

    if data_list is None:
        return product_info_l

    for data in data_list:
        try:
            if "products" in data:
                products_list = data["products"]
                for product_name in products_list:
                    product = get_product_by_name(product_name)
                    if product:
                        product_info_l.append(product)
                    else:
                        print(f"Error: Product '{product_name}' not found")
            elif "category" in data:
                category_name = data["category"]
                category_products = get_products_by_category(category_name)
                for product in category_products:
                    product_info_l.append(product)
            else:
                print("Error: Invalid object format")
        except Exception as e:
            print(f"Error: {e}")

    return product_info_l


def read_string_to_list(input_string: str) -> List[Dict[str, Any]]:
    """
    Takes a str that has a list of dictionary where keys are categories and each value is a list of product names in that category, converts the str to list and returns it.
    """

    if input_string is None:
        return None

    try:
        input_string = input_string.replace(
            "'", '"'
        )  # Replace single quotes with double quotes for valid JSON
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None


def generate_output_string(data_list: List[Dict[str, Any]]) -> str:
    """
    Returns a string that has a list of dictionary of product details, these details are fetched for products/categories in data_list.
    """
    output_string = ""

    if data_list is None:
        return output_string

    for data in data_list:
        try:
            if "products" in data:
                products_list = data["products"]
                for product_name in products_list:
                    product = get_product_by_name(product_name)
                    if product:
                        output_string += json.dumps(product, indent=4) + "\n"
                    else:
                        print(f"Error: Product '{product_name}' not found")
            elif "category" in data:
                category_name = data["category"]
                category_products = get_products_by_category(category_name)
                for product in category_products:
                    output_string += json.dumps(product, indent=4) + "\n"
            else:
                print("Error: Invalid object format")
        except Exception as e:
            print(f"Error: {e}")

    return output_string


# Example usage:
# product_information_for_user_message_1 = generate_output_string(category_and_product_list)
# print(product_information_for_user_message_1)


def answer_user_msg(user_msg: str, product_info: List[Dict[str, Any]]) -> str:
    """
    Returns a string from LLM containing product details extracted from product_info for products in user_msg.
    """
    delimiter = "####"
    system_message = f"""
    You are a customer service assistant for a large electronic store. \
    Respond in a friendly and helpful tone, with concise answers. \
    Make sure to ask the user relevant follow up questions.
    """
    # user_msg = f"""
    # tell me about the smartx pro phone and the fotosnap camera, the dslr one. Also what tell me about your tvs"""
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"{delimiter}{user_msg}{delimiter}"},
        {
            "role": "assistant",
            "content": f"Relevant product information:\n{product_info}",
        },
    ]
    response = get_completion_from_messages(messages)
    return response
