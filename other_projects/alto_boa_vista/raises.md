# Estrutura para raises

## ConstructorException

### Code 01 [0]

    f"Two equal elements!"
    f"Invalid terminals {terminal_id} / rates"
    f"It's not allowed two elements with the same 'product', 'operation', and 'modal'"`
    f"Try: ."

### Code 02 [1, 5, 7, 12, 14, 15=16]

    f"Missing information!"
    f"It's necessary 'missing_information' for 'where'."
    f"Try: Include information of {missing_information} {details_missing_information} at {details_where}."

    f"Missing information!"
    f"It's necessary 'rates' for each product allowed by terminal."
    f"Try: Include information of rates at terminal {terminal_id}."

    f"Missing information!"
    f"It's necessary 'month' for each flow element."
    f"Try: Include information of month {month} at flow element {flow_id}."

    f"Missing information!"
    f"It's necessary 'data of train volume' for each product in origin."
    f"Try: Include information of train volume at product {demand['product']}, origin {demand['origin_name']} ({demand['origin']})."

    f"Missing information!"
    f"It's necessary 'cradle' for each vessel product."
    f"Try: Include information of cradle at vessel product {vessel['name']}."

    f"Missing information!"
    f"It's necessary 'assets data' in Bottleneck."
    f"Try: Include information of 'assets' data."

    f"Missing information!"
    f"It's necessary {type_name} in Bottleneck."
    f"Try: Include information of {type_name} data."

### Code 03 [2, 4]

    f"Element not found!"
    f"Element class {element_name}: {id}"
    f"Not found in railroad / wagon_cycles."
    f"Try: ."

    f"Element not found!"
    f"Terminal {name}: {t_id}" 
    f"Not found in railroad / wagon_cycles."
    f"Try: ."

    f"Element not found!"
    f"Third {site} {name}: {t_id}"
    f"Not found in railroad / wagon_cycles."
    f"Try: ."

### Code 04 [6, 8, 9, 10]
    
    f"Wrong Information!"
    f"Wrong {what is wrong}."
    f"{What are the conditions?}"
    f"Try: ."

    f"Wrong Information!"
    f"Wrong number of weeks in demand in month {month}."
    f"Size of demand_month_info[month] must be equal n_weeks."
    f"Try: ."

    f"Wrong Information!"
    f"Wrong load_proportion."
    f"Load proportion can't be equal to zero"
    f"Try: Readjust demand at {}"

    f"Wrong Information!"
    f"Wrong origin or destination."
    f"Origin {origin} and destination {destination} must be an created terminal or port."
    f"Try: Review demand {elem['flow']} data."

    f"Wrong Information!"
    f"Wrong demand for the flow {elem['flow']}."
    f"The product {elem['product']} must be allowed by the origin {elem['origin_name']} ({elem['origin']})"
    f"Try: Review demand {elem['flow']} data."

### Code 05 [11, 13]

    f"Fail of Verification!"
    f"Invalid {element}"
    f"Error in verifying {what}"
    f"Informations: {informations}"
    f"Try: ."

    f"Fail of Verification!"
    f"Invalid Connectivity!"
    f"Error in verifying connectivity between cradles and warehouses."
    f"Informations: (id do armazem " + w_id + ")"
    f"Try: ."

    f"Fail of Verification!"
    f"Invalid Port!"
    f"Error in verifying if every products of port are operated in some cradle"
    f"Informations:  Port {port['id']}, {repr(prod)}
    f"Try: ."


