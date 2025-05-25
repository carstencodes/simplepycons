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


class FormbricksIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "formbricks"

    @property
    def original_file_name(self) -> "str":
        return "formbricks.svg"

    @property
    def title(self) -> "str":
        return "Formbricks"

    @property
    def primary_color(self) -> "str":
        return "#00C4B8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Formbricks</title>
     <path d="M8.658 0a5.714 5.714 0 0 0-5.715 5.714v1.532h14.49a3.623
 3.623 0 0 0 0-7.246ZM2.943 8.377v7.246h14.49a3.623 3.623 0 0 0
 0-7.246zm0 8.377v3.623a3.623 3.623 0 0 0 7.246 0v-3.623z" />
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
