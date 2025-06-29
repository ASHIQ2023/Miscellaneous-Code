def module_docs(module_name=None):

    """Display documentation for all functions in a module"""
    
    # Get module name from user if not provided
    if module_name is None:
        module_name = input('Enter the name of the module: ')
    
    try:
        # Import the module dynamically
        import importlib

        module = importlib.import_module(module_name)
        
        print(f"\nDocumentation for module: {module_name}")
        print("=" * 50)
        
        docs_found = []
        
        for item in dir(module):
            if not item.startswith('_'):
                print(f"\n{item}:")
                try:
                    attr = getattr(module, item)
                    doc = attr.__doc__
                    if doc:
                        print(doc)
                        docs_found.append((item, doc))
                    else:
                        print("No documentation available")
                        docs_found.append((item, "No documentation available"))
                except:
                    print("No documentation available")
                    docs_found.append((item, "No documentation available"))
        
        return docs_found
        
    except ImportError:
        print(f"Module '{module_name}' not found")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
