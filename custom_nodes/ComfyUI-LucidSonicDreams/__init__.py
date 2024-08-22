from .modules.lucid_sonic_dreams_node import InputParamLucid, APICallNode, SimpleSaveVideoNode, SaveVideoTEST, LoadVideotest

NODE_CLASS_MAPPINGS = {
    "InputParamLucid": InputParamLucid,
    "APICallNode": APICallNode,
    "SimpleSaveVideoNode" : SimpleSaveVideoNode,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "InputParamLucid": "Input Parameters Lucid",
    "APICallNode": "Api Call Node",
    "SimpleSaveVideoNode": "Simple Save Video Node",
}


print("\033[35m")
print("  Lucid loaded!  ")
print("\033[0m")