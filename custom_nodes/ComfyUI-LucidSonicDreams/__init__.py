from .modules.lucid_sonic_dreams_node import InputParamLucid, APICallNode

NODE_CLASS_MAPPINGS = {
    "InputParamLucid": InputParamLucid,
    "APICallNode": APICallNode,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "InputParamLucid": "Input Parameters Lucid",
    "APICallNode": "Api Call Node",
    
}


print("\033[35m")
print("  Lucid loaded!  ")
print("\033[0m")