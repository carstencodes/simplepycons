#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class LiningIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lining"

    @property
    def original_file_name(self) -> "str":
        return "lining.svg"

    @property
    def title(self) -> "str":
        return "Li-Ning"

    @property
    def primary_color(self) -> "str":
        return "#C5242C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Li-Ning</title>
     <path d="M8.926
 8.815c-.261-.004-.696.011-1.422.084-1.937.194-2.398.828-2.398.828L0
 15.177h1.017c4.279-4.664 8.291-6.278
 8.291-6.278s.052-.075-.382-.084Zm2.332
 1.571c-1.71-.008-3.181.092-3.803.366-1.422.625-3.838 2.271-6.035
 4.425 0 0 .864.115 1.902-.48 0 0 3.416-2.586 6.165-2.07 2.75.516
 5.169 1.829 5.169 1.829s1.751 1 3.39.438c1.64-.563 5.954-2.898
 5.954-2.898s-3.266-.776-6.265-1.182c-1.687-.229-4.279-.418-6.477-.428Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
