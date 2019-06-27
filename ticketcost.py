def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    total_ticket_cost=(((no_of_adults*37550.0)+(37550.0/3*no_of_children))+(((no_of_adults*37550.0)+(37550.0/3*no_of_children))*0.07)-(((no_of_adults*37550.0)+(37550.0/3*no_of_children))+
    (((no_of_adults*37550.0)+(37550.0/3*no_of_children))*0.07))*0.1)
 return total_ticket_cost
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
