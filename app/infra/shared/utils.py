def subclass_hook_return(subclass):
    return (hasattr(subclass, 'load_data_source') and
     callable(subclass.load_data_source) and
     hasattr(subclass, 'extract_text') and
     callable(subclass.extract_text) or
     NotImplemented)
