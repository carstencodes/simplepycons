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


class BaserowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "baserow"

    @property
    def original_file_name(self) -> "str":
        return "baserow.svg"

    @property
    def title(self) -> "str":
        return "Baserow"

    @property
    def primary_color(self) -> "str":
        return "#5190EF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Baserow</title>
     <path d="M1.291.068A1.29 1.29 0 0 0 0 1.36v3.352a1.29 1.29 0 0 0
 1.291 1.291h3.354a1.29 1.29 0 0 0 1.289-1.291V1.359A1.29 1.29 0 0 0
 4.644.07Zm9.033 0a1.29 1.29 0 0 0-1.29 1.291v3.352a1.29 1.29 0 0 0
 1.29 1.291H22.71A1.29 1.29 0 0 0 24 4.711V1.359A1.29 1.29 0 0 0
 22.709.07ZM1.291 9.033A1.29 1.29 0 0 0 0 10.323v3.353a1.29 1.29 0 0 0
 1.291 1.29h21.418A1.29 1.29 0 0 0 24 13.677v-3.354a1.29 1.29 0 0
 0-1.291-1.289Zm0 8.965A1.29 1.29 0 0 0 0 19.289v3.352a1.29 1.29 0 0 0
 1.291 1.29h12.385a1.29 1.29 0 0 0 1.29-1.29v-3.352a1.29 1.29 0 0
 0-1.29-1.291zm18.064 0a1.29 1.29 0 0 0-1.289 1.291v3.352a1.29 1.29 0
 0 0 1.29 1.29h3.353A1.29 1.29 0 0 0 24 22.642v-3.352a1.29 1.29 0 0
 0-1.291-1.291z" />
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
