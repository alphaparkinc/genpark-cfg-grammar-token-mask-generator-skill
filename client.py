"""CFG Grammar Token Mask Generator.
100% Python Standard Library.
"""

class CFGTokenMaskGenerator:
    """Computes allowable next character/token masks from simple EBNF grammar states."""
    TRANSITIONS = {
        "START": {"{": "IN_OBJECT", "[": "IN_ARRAY", "\"": "IN_STRING"},
        "IN_OBJECT": {"\"": "IN_KEY", "}": "END"},
        "IN_KEY": {"\"": "AFTER_KEY"},
        "AFTER_KEY": {":": "EXPECT_VALUE"},
        "EXPECT_VALUE": {"\"": "IN_VALUE_STRING", "0": "IN_NUM", "1": "IN_NUM", "t": "IN_BOOL", "f": "IN_BOOL", "{": "IN_OBJECT", "[": "IN_ARRAY"},
        "IN_VALUE_STRING": {"\"": "AFTER_VALUE"},
        "AFTER_VALUE": {",": "IN_OBJECT", "}": "END"}
    }

    @classmethod
    def get_allowed_next(cls, current_state: str) -> list:
        trans = cls.TRANSITIONS.get(current_state, {})
        return list(trans.keys())

    @classmethod
    def transition(cls, current_state: str, char: str) -> str:
        trans = cls.TRANSITIONS.get(current_state, {})
        return trans.get(char, "ERROR")
