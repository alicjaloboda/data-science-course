import grocerystore.store_service as store_service

items_to_purchase = {
    'candy': 7,
    'notebook': 15,
    'paper':8,
    'coffee': 3,
    'socks': 7
}

user_money = int(input('How much money do you have? '))

items_price_added_to_card = []
user_shopping = False

while not user_shopping:
    add_item_to_cart = input('What item would you like to add to your cart? ')
    
    #Check if key exists
    if add_item_to_cart.lower().strip() in items_to_purchase:
        items_price_added_to_card.append(items_to_purchase.get(add_item_to_cart))
    
        print(f'You currently have {len(items_price_added_to_card)} ' f'items in your cart.')
    else:
        print('Item is not at this store')
        continue
    
    keep_shopping = input('Would you like to continue shopping? (Y = yes, N = no) ')

    if keep_shopping.lower().strip() == 'n':
        user_shopping = True

store_service.purchase_items(user_money_arg=user_money, items=items_price_added_to_card)

