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


class ThreemaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "threema"

    @property
    def original_file_name(self) -> "str":
        return "threema.svg"

    @property
    def title(self) -> "str":
        return "Threema"

    @property
    def primary_color(self) -> "str":
        return "#3FE669"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Threema</title>
     <path d="M11.998 20.486a1.757 1.757 0 1 1 0 3.514 1.757 1.757 0 0
 1 0-3.514zm-6.335 0a1.757 1.757 0 1 1 0 3.514 1.757 1.757 0 0 1
 0-3.514zm12.671 0a1.757 1.757 0 1 1 0 3.514 1.757 1.757 0 0 1
 0-3.514zM12 0c5.7 0 10.322 4.066 10.322 9.082 0 5.016-4.622
 9.083-10.322 9.083a11.45 11.45 0 0 1-4.523-.917l-5.171 1.293
 1.105-4.42c-1.094-1.442-1.733-3.175-1.733-5.039C1.678 4.066 6.3 0 12
 0zm-.001 4.235A2.926 2.926 0 0 0 9.072 7.16v1.17h-.115a.47.47 0 0
 0-.47.47v4.126c0 .26.21.471.47.471h6.086c.26 0
 .47-.21.47-.47V8.798a.47.47 0 0 0-.47-.47h-.115v-1.17a2.927 2.927 0 0
 0-2.93-2.924zm0 1.17c.972 0 1.758.786 1.758
 1.754v1.17h-3.514v-1.17c0-.968.786-1.754 1.756-1.754z" />
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
