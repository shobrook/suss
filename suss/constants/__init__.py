try:
    from suss.constants.languages import LANGUAGE_EXTENSIONS
    from suss.constants.boilerplate import BOILERPLATE_REGEXES
    from suss.constants.agent import (
        MAX_MERGE_DISTANCE,
        CODE_SEARCH_LIMIT,
        FILE_SEARCH_LIMIT,
        MAX_CONTEXT_TOKENS,
        MAX_TOOL_CALLS,
        MAX_THINKING_TOKENS,
    )
except ImportError:
    from constants.languages import LANGUAGE_EXTENSIONS
    from constants.boilerplate import BOILERPLATE_REGEXES
    from constants.agent import (
        MAX_MERGE_DISTANCE,
        CODE_SEARCH_LIMIT,
        FILE_SEARCH_LIMIT,
        MAX_CONTEXT_TOKENS,
        MAX_TOOL_CALLS,
        MAX_THINKING_TOKENS,
    )
