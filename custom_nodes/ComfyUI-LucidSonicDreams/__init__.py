from .modules.lucid_sonic_dreams_node import InputParamLucid, APICallNode, SimpleSaveVideoNode, InputParamLucidSecond

NODE_CLASS_MAPPINGS = {
    "InputParamLucid": InputParamLucid,
    "APICallNode": APICallNode,
    "SimpleSaveVideoNode" : SimpleSaveVideoNode,
    "InputParamLucidSecond" : InputParamLucidSecond,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "InputParamLucid": "Input Parameters Lucid",
    "APICallNode": "Api Call Node",
    "SimpleSaveVideoNode": "Simple Save Video Node",
    "InputParamLucidSecond":"Input Parameters Lucid Second"
}


print("\033[35m")
print("  Lucid loaded!  ")
print("\033[0m")