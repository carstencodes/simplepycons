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


class HaskellIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "haskell"

    @property
    def original_file_name(self) -> "str":
        return "haskell.svg"

    @property
    def title(self) -> "str":
        return "Haskell"

    @property
    def primary_color(self) -> "str":
        return "#5D4F85"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Haskell</title>
     <path d="M0 3.535L5.647 12 0 20.465h4.235L9.883 12 4.235
 3.535zm5.647 0L11.294 12l-5.647 8.465h4.235l3.53-5.29 3.53
 5.29h4.234L9.883 3.535zm8.941 4.938l1.883 2.822H24V8.473zm2.824
 4.232l1.882 2.822H24v-2.822z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://wiki.haskell.org/Thompson-Wheeler_log'''

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
