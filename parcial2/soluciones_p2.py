def f2(func):
    error_count = 0
    
    def wrapper(*args, **kwargs):
        nonlocal error_count
        if error_count >= 3:
            print("> Leer la documentacion")
            return None
        
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_count += 1
            print(f"> Ha cometido {error_count} error(es): {type(e).__name__}")
            return None
            
    return wrapper
