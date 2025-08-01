class order:
    def __init__(self,customer_name,order,total_amount,discount):
        self.customer_name=customer_name
        self.order=order
        self.__total_amount=total_amount
        self.__discount=discount
    
    def __final_rate(self):
        return self.__total_amount-self.__discount
    
    def _get_admin_view(self):
        return{
            "Customer" :self.customer_name,
            "Order ":self.order,
            "Total Amount":f"{self.__total_amount}",
            "Discount Amount":f"{self.__discount}"
        }
    def _get_customer_view(self):
        return{
            "Customer" :self.customer_name,
            "Order ":self.order,
            "Final Rate":f"{self.__final_rate()}"
        }
putin=order('pradeep','pizza',180,50)
print(putin._get_admin_view())
print(putin._get_customer_view())