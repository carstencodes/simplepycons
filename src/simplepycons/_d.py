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


class DIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "d"

    @property
    def original_file_name(self) -> "str":
        return "d.svg"

    @property
    def title(self) -> "str":
        return "D"

    @property
    def primary_color(self) -> "str":
        return "#B03931"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>D</title>
     <path d="M22.635 3.883a1.364 1.25 0 0 0-1.363 1.25 1.364 1.25 0 0
 0 1.363 1.25A1.364 1.25 0 0 0 24 5.133a1.364 1.25 0 0
 0-1.365-1.25zm-16.004.418-6.027.008c-.026 0-.051-.003-.076
 0-.296.036-.527.273-.528.558l.018 14.574c0
 .22.06.676.682.676l5.58-.021c1.595-.003 2.664-.031
 3.3-.112h.016a11.43 11.43 0 0 0 1.955-.469c1.22-.38 2.3-.944
 3.23-1.697a7.854 7.854 0 0 0 2.114-2.562 6.716 6.716 0 0 0 .646-1.987
 4.244 3.89 0 0 0 .26.028 4.244 3.89 0 0 0 4.244-3.89 4.244 3.89 0 0
 0-4.244-3.89 4.244 3.89 0 0 0-2.9 1.082 8.838 8.838 0 0
 0-2.25-1.355c-1.536-.65-3.536-.948-6.02-.943zm-.262 3.004c1.215-.003
 2.079.034 2.569.101a7.32 7.32 0 0 1 1.617.436c.57.218 1.068.483
 1.496.814 1.177.915 1.732 1.999 1.734 3.432.003 1.468-.534 2.611-1.68
 3.57a5.582 5.582 0 0
 1-1.177.742c-.409.19-.942.355-1.615.496-.636.128-1.6.2-2.856.202l-2.673.004-.012-9.793
 2.598-.004z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dlang/dlang.org/blob/6d0e2'''

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
