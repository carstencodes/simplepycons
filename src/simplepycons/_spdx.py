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


class SpdxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spdx"

    @property
    def original_file_name(self) -> "str":
        return "spdx.svg"

    @property
    def title(self) -> "str":
        return "SPDX"

    @property
    def primary_color(self) -> "str":
        return "#4398CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SPDX</title>
     <path d="M0 0v24H8.222l2.089-2.373
 2.09-2.374V13.2H18.978l2.51-2.488L24 8.223V0H12zm5.2 5.2h13.791L12.2
 12c-3.735 3.74-6.838 6.8-6.896 6.8-.057 0-.104-3.06-.104-6.8zm8.4
 8.8v10H24V14h-5.2z" />
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
