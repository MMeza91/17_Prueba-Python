def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    division = n_pregunta/p_level
    if division <= 1:
        level = "básicas"
    elif division > 1 and division <= 2:
        level = "intermedias"
    else:
        level = "avanzadas"
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias